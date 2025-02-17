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

class Bookings(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.OneToOneField(Seat, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    booking_date = models.DateField(blank=True, null=True)

    #automatically mark seat as booked when a new booking is created - for testing
    #overriding save()
    def save(self, *args, **kwargs):
        #save booking with the super class's save()
        super().save(*args, **kwargs)
        #set the seat's is_booked to true
        self.seat.is_booked = True
        #save that to the database
        self.seat.save()

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} - Seat {self.seat.seat_number}"