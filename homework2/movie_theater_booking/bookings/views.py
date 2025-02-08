from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from .models import Movie, Seat, Bookings
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# Create your views here.
'''
MovieViewSet: For CRUD operations on movies.
SeatViewSet: For seat availability and booking.
BookingViewSet: For users to book seats and view their booking history.
'''

class MovieViewSet(viewsets.ModelViewSet):
    """
    Provides CRUD operations for movies.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class SeatViewSet(viewsets.ModelViewSet):
    """
    Handles seat availability and booking updates.
    """
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    @action(detail=True, methods=['post'])
    def book(self, request, pk=None):
        """
        Custom action to book a seat.
        """
        seat = get_object_or_404(Seat, pk=pk)
        if seat.is_booked:
            return Response({"message": "This seat is already booked."}, status=status.HTTP_400_BAD_REQUEST)

        seat.is_booked = True
        seat.save()
        return Response({"message": "Seat successfully booked."}, status=status.HTTP_200_OK)


class BookingViewSet(viewsets.ModelViewSet):
    """
    Allows users to book seats and view their booking history.
    """
    queryset = Bookings.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        """
        Custom booking logic: Ensures seat isn't already booked.
        """
        movie_id = request.data.get('movie')
        seat_id = request.data.get('seat')
        user_id = request.data.get('user')

        seat = get_object_or_404(Seat, pk=seat_id)

        if seat.is_booked:
            return Response({"message": "This seat is already booked."}, status=status.HTTP_400_BAD_REQUEST)

        booking = Bookings.objects.create(movie_id=movie_id, seat_id=seat_id, user_id=user_id)
        seat.is_booked = True
        seat.save()

        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

    def get_queryset(self):
        """
        Filter bookings by user if a 'user_id' is provided in the query params.
        """
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Bookings.objects.filter(user_id=user_id)
        return super().get_queryset()