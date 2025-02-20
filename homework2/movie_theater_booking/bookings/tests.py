from django.test import TestCase
from django.contrib.auth.models import User
from .models import Movie, Seat, Bookings
from rest_framework.test import APIClient
from rest_framework import status
from datetime import date

#######################
# Class-based Testing #
#######################

class ModelTests(TestCase):
    def setUp(self):
        #create a user, movie, and seat
        self.user = User.objects.create_user(username='testuser', password='testpass')
        self.movie = Movie.objects.create(
            title="Sample Movie", 
            description="A great movie.", 
            release_date=date.today(), 
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="120", is_booked=False)

    def test_user_creation(self):
        #testing that user was created in database
        self.assertTrue(User.objects.filter(username='testuser').exists())
        #testing that the user is not a superuser
        self.assertFalse(self.user.is_superuser)

    def test_movie_creation(self):
        #testing that movie was created in database
        self.assertTrue(Movie.objects.filter(title="Sample Movie", description="A great movie.", release_date=date.today(), duration=120).exists())

    def test_seat_creation(self):
        #testing that seat was created in database
        self.assertTrue(Seat.objects.filter(seat_number="120", is_booked=False).exists())    

    def test_booking_creation(self):
        #create a booking
        booking = Bookings.objects.create(movie=self.movie, seat=self.seat, user=self.user, booking_date=date.today())

        #testing that user was created in database
        self.assertTrue(Bookings.objects.filter(movie=self.movie, seat=self.seat, user=self.user, booking_date=date.today()).exists())
        
        #see if the str() method of the Booking object was initialized as expected
        self.assertEqual(str(booking), "testuser - Sample Movie - Seat 120")

    def test_double_booking_prevention(self):
        #creates a booking and then tries to create an identical booking
        Bookings.objects.create(movie=self.movie, seat=self.seat, user=self.user, booking_date=date.today())
        with self.assertRaises(Exception):  #should fail since seat is already booked
            Bookings.objects.create(movie=self.movie, seat=self.seat, user=self.user, booking_date=date.today())

    def test_seat_is_booked(self):
        #check if seat was booked to start
        self.assertFalse(self.seat.is_booked)

        #create a model through the objects.create() method
        booking = Bookings.objects.create(movie=self.movie, seat=self.seat, user=self.user, booking_date=date.today())

        #refresh the database and see if the seat was marked as booked
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.is_booked)

class APITests(TestCase):
    '''
    Use APIClient to make requests:
    Instantiate APIClient in your test methods or setUp method.
    Use methods like client.get(), client.post(), client.put(), client.delete() to simulate HTTP requests.
    Pass data as needed for POST, PUT, and PATCH requests.
    '''
    #create an API client, user, movie, and seat
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='apiuser', password='testpass')
        #login to the client with the User login
        self.client.login(username='apiuser', password='testpass')
        self.movie = Movie.objects.create(
            title="API Movie", 
            description="An API tested movie.", 
            release_date=date.today(), 
            duration=130
        )
        self.seat = Seat.objects.create(seat_number="100", is_booked=False)

    #see if the /api/movies/ page is accessible
    def test_get_movies(self):
        response = self.client.get("/api/movies/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #see if the /api/seats/ page is accessible
    def test_get_seats(self):
        response = self.client.get("/api/seats/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #see if the /api/bookings/ page is accessible
    def test_get_bookings(self):
        response = self.client.get("/api/bookings/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    #CREATE - movie testing for CRUD
    def test_movie_creation_api(self):
        response = self.client.post("/api/movies/", {
            "title": "Sample Movie", 
            "description": "A great movie.", 
            "release_date": date.today(), 
            "duration": 120
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #refresh database
        self.movie.refresh_from_db()

        #testing that movie was created in database
        self.assertTrue(Movie.objects.filter(title="Sample Movie", description="A great movie.", release_date=date.today(), duration=120).exists())

    #READ - movie testing for CRUD
    def test_movie_read_api(self):
        #go to the page of a specific movie by using the id in the URL
        response = self.client.get(f"/api/movies/{self.movie.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        #check the response data to see if the correct movie was grabbed and was readable
        self.assertEqual(response.data["title"], self.movie.title)
        self.assertEqual(response.data["description"], self.movie.description)
        self.assertEqual(response.data["duration"], self.movie.duration)

    #UPDATE - movie testing for CRUD
    def test_movie_update_api(self):
        #go to the page of a specific movie by using the id in the URL
        #by using PUT, can now update that specific movie
        response = self.client.put(f"/api/movies/{self.movie.id}/", {
            "title": "Updated Movie",
            "description": "Updated description.",
            "release_date": date.today(),
            "duration": 150
        }, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.movie.refresh_from_db()

        #check the response data to see if the correct movie was updated as expected
        self.assertEqual(self.movie.title, "Updated Movie")
        self.assertEqual(self.movie.description, "Updated description.")
        self.assertEqual(self.movie.duration, 150)

    #DELETE - movie testing for CRUD
    def test_movie_delete_api(self):
        #go to the page of a specific movie by using the id in the URL
        #by using DELETE, can now remove that specific movie
        response = self.client.delete(f"/api/movies/{self.movie.id}/")
        #should recieve the DELETE response code from the server
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        #check database for the movie
        self.assertFalse(Movie.objects.filter(id=self.movie.id).exists())

    def test_seat_creation_api(self):
        response = self.client.post("/api/seats/", {
            "seat_number": "120", 
            "is_booked": False
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #refresh database
        self.movie.refresh_from_db()

        #testing that seat was created in database
        self.assertTrue(Seat.objects.filter(seat_number="120", is_booked=False).exists())  

    def test_booking_creation_api(self):
        response = self.client.post("/api/bookings/", {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id,
            "booking_date": str(date.today())
        })

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        #refresh database
        self.movie.refresh_from_db()

        #testing that seat was created in database
        self.assertTrue(Bookings.objects.filter(movie=self.movie, seat=self.seat, user=self.user, booking_date=date.today()).exists())

    #see if creating a booking from the api works as expected (books a seat)
    def test_booking_caused_book_seat(self):
        #check if seat was booked to start
        self.assertFalse(self.seat.is_booked)

        response = self.client.post("/api/bookings/", {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id,
            "booking_date": str(date.today())
        })

        #seat should only be booked after the creation of the booking
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.is_booked)

    #see if users can make a double booking
    def test_prevent_double_booking(self):
        Bookings.objects.create(movie=self.movie, seat=self.seat, user=self.user, booking_date=date.today())
        response = self.client.post("/api/bookings/", {
            "movie": self.movie.id,
            "seat": self.seat.id,
            "user": self.user.id,
            "booking_date": str(date.today())
        })
        #the response SHOULD cause an error because we prevented the double booking
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
