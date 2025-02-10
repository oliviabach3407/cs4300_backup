from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=30)

class Movie(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=500)
    release_date = models.DateField()
    duration = models.IntegerField()

class Seat(models.Model):
    seat_number = models.CharField(max_length=30)
    is_booked = models.BooleanField(default=False)

class Bookings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateTimeField()