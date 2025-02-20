from rest_framework import viewsets, status
from rest_framework.response import Response
from django.template.response import TemplateResponse

from django.shortcuts import get_object_or_404, render, redirect
from .models import Movie, Seat, Bookings
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

############
# Viewsets #
############

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

        #checking if the booking object already exists in the database
        if Bookings.objects.filter(seat=seat, movie=movie, booking_date=booking_date).exists():
            return Response({"error": "Seat already booked for this movie and time."}, status=status.HTTP_400_BAD_REQUEST)

        #create the object with the given information (automatically "saved")
        #set the seat to booked (redundant because of what I did in my model)
        #save the seat
        booking = Bookings.objects.create(movie=movie, seat=seat, user_id=user_id, booking_date=booking_date)
        seat.is_booked = True
        seat.save()

        #manually return the 201 response so that we can see that something was CREATED
        return Response(BookingSerializer(booking).data, status=status.HTTP_201_CREATED)

    #overriding built in get_queryset to be able to filter by user_id
    def get_queryset(self):
        """ Filter bookings by user if `user_id` is provided. """
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Bookings.objects.filter(user_id=user_id)
        return super().get_queryset()
    
########################
# Template-based Views #
########################

#path('', view_movies, name='movies')
#simple - doesn't need to be sent any parameters
def view_movies(request):
    movies = Movie.objects.all() #gets all movie objects that exist from the db

    #sending request, page name, and data {}
    return render(request, 'movie_list.html', {"movies": movies})

#path('book-seat/<int:movie_id>/', book_seat, name='book_seat'),
#complicated - need to accept movie_id as a parameter
#require login so that can be linked to a specific User
@login_required
def book_seat(request, movie_id):
    #get movie from database with movie_id that was passed
    movie = get_object_or_404(Movie, id=movie_id)
    #get all seats that aren't booked from the database
    available_seats = Seat.objects.filter(is_booked=False)

    #request will be POST if user clicked the submit button
    #<form method="post">
    #<button type="submit" class="btn btn-primary btn-sm float-end">Confirm Booking</button>
    if request.method == "POST":
        #get the information from the form (user selected these things)
        seat_id = request.POST.get('seat_id')
        booking_date = request.POST.get('booking_date')

        #link seat_id to the actual seat in the database
        seat = get_object_or_404(Seat, id=seat_id)

        #double check that the seat wasn't already booked
        if not seat.is_booked:
            #create the booking
            Bookings.objects.create(movie=movie, seat=seat, user=request.user, booking_date=booking_date)

            #mark seat as booked
            seat.is_booked = True
            seat.save()

        #if seat was successfully booked and booking was created - redirect to booking_history URL
        return redirect('booking_history')

    #if we didn't sense a POST request (basically if we reloaded the page or had an invalid form)
    return render(request, 'seat_booking.html', {'movie': movie, 'seats': available_seats})

#path('booking-history/', booking_history, name='booking_history'),
#simple - doesn't need to be sent any parameters
#login is required because we need to link the bookings to THIS User
@login_required
def booking_history(request):
    #filter bookings by logged-in user
    bookings = Bookings.objects.filter(user=request.user)

    #sending request, page name, and data {}
    return render(request, 'booking_history.html', {"bookings": bookings})

########################
# Authentication Views #
########################

#path('signup/', signup, name='signup'), 
def signup(request):
    #again this is relying on a form submission (waiting for a user to submit their information)
    if request.method == "POST":
        #convert our HTML form into a UserCreationForm
        form = UserCreationForm(request.POST)
        #converts data into a normal User object in the database
        if form.is_valid():
            user = form.save()
            login(request, user)  #log the user in after signup
            #redirect to home/movies page
            return redirect('movies')  
    else:
        #else we want to empty the form
        form = UserCreationForm()
    
    #else render the signup page again
    return render(request, 'signup.html', {'form': form})