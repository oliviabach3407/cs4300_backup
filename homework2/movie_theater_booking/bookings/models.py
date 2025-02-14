from django.db import models
from django.contrib.auth.models import User #using django's built-in user

class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    release_date = models.DateField()
    duration = models.IntegerField()

class Seat(models.Model):
    seat_number = models.CharField(max_length=30)
    is_booked = models.BooleanField(default=False)

    #added this so that seats can be linked to movies
    #otherwise all movies share the same bank of seats
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    #MIGHT NEED TO ADD A DATE FIELD TOO - COMPARE TO EXISTING DATE FIELDS
    #you might need to rework this so all comparisons are done through 
    #the bookings class instead of through seats (including movie)

class Bookings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - Seat {self.seat.seat_number}"