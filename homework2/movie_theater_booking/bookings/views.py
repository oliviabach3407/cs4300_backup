from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Movie, Seat, Bookings
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

class MovieViewSet(viewsets.ModelViewSet):
    """ Provides CRUD operations for movies. """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    """ Handles seat availability. """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

class BookingViewSet(viewsets.ModelViewSet):
    """ Handles seat bookings. """
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        """ Ensures seat isn't already booked before creating a booking. """
        movie_id = request.data.get('movie')
        seat_id = request.data.get('seat')
        user_id = request.data.get('user')
        booking_date = request.data.get('booking_date')

        seat = get_object_or_404(Seat, pk=seat_id)
        movie = get_object_or_404(Movie, pk=movie_id)

        if Bookings.objects.filter(seat=seat, movie=movie, booking_date=booking_date).exists():
            return Response({"error": "Seat already booked for this movie and time."}, status=status.HTTP_400_BAD_REQUEST)

        booking = Bookings.objects.create(movie=movie, seat=seat, user_id=user_id, booking_date=booking_date)
        seat.is_booked = True
        seat.save()

        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        """ Filter bookings by user if `user_id` is provided. """
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Bookings.objects.filter(user_id=user_id)
        return super().get_queryset()