from rest_framework import viewsets, status
from rest_framework.response import Response
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.utils.dateparse import parse_date #helps with user input

from django.shortcuts import get_object_or_404, render, redirect
from .models import Movie, Seat, Bookings, User
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer, UserSerializer

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

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

@login_required
def book_seat(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    available_seats = Seat.objects.filter(movie=movie, is_booked=False)

    if request.method == "POST":
        seat_id = request.POST.get('seat_id')
        booking_date = request.POST.get('booking_date')  # Get selected date
        seat = get_object_or_404(Seat, id=seat_id, is_booked=False)

        # Ensure the date is valid
        if not booking_date:
            return render(request, 'seat_booking.html', {'movie': movie, 'seats': available_seats, 'error': 'Invalid date selected!'})

        # Check if the seat is already booked for this date
        if Bookings.objects.filter(seat=seat, booking_date=booking_date).exists():
            return render(request, 'seat_booking.html', {'movie': movie, 'seats': available_seats, 'error': 'Seat already booked for this date!'})

        # Create the booking
        Bookings.objects.create(movie=movie, seat=seat, user=request.user, booking_date=booking_date)

        # Mark seat as booked
        seat.is_booked = True
        seat.save()

        return redirect('booking_history')

    return render(request, 'seat_booking.html', {'movie': movie, 'seats': available_seats})
    
@login_required
def booking_history(request):
    bookings = Bookings.objects.filter(user=request.user)  # Filter by logged-in user
    return render(request, 'booking_history.html', {"bookings": bookings})

########################
# Authentication Views #
########################

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after signup
            return redirect('movies')  
    else:
        form = UserCreationForm()
    
    return render(request, 'signup.html', {'form': form})