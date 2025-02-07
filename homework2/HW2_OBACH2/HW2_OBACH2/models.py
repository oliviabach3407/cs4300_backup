from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    showtimes = models.TimeField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return f"{self.title}"

class Booking(models.Model):
    user = models.CharField(max_length=100)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat_number = models.IntegerField()

    def __str__(self):
        return f"{self.user}: {self.movie}, Seat: {self.seat_number}"