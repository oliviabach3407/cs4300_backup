from rest_framework import viewsets, status
from rest_framework.response import Response
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from .models import Movie, Seat, Bookings, User
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer, UserSerializer


############
# Viewsets #
############
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

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

    def create(self, request):
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
    
########################
# Template-based Views #
########################
'''
    path('movies/', view_movies.asView(), name="movies"),
    path('book-seat/', book_seat.asView(), name="book-seat"),
    path('booking-history/', booking_history.asView(), name="booking-history"),
'''

def view_movies(request):
    movies = Movie.objects.all() #gets all movie objects that exist

    return TemplateResponse(request, 'movie_list.html', {"movies": movies})

def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    users = User.objects.all()
    seats = Seat.objects.filter(is_booked=False)

    if request.method == "GET":
        return render(request, 'seat_booking.html', {'movie': movie, 'seats': seats, 'users': users})
    
    if request.method == 'POST':
        seat_number = request.Post.get('seat_number')
        seat = get_object_or_404(Seat, seat_number=seat_number)
        user_name = request.POST.get('user_name')
        user = get_object_or_404(User, name=user_name)

        Bookings.objects.create(movie=movie, seat=seat, user=user)

        seat.is_booked = True
        seat.save()

        return redirect('booking_history')
    
def booking_history(request, user_id):
    bookings = Bookings.objects.all()

    return render(request, 'booking_history.html', {"bookings": bookings})
