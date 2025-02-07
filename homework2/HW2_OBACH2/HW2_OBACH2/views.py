from django.http import JsonResponse
from django.views import View 
from HW2_OBACH2.models import Movie
from HW2_OBACH2.models import Booking

#Viewing a list of available movies
class AvailableMovies(View):
    def get(self, request):
        movies = Movie.objects.all()

        #each dictionary represents one movie
        serialized_data = [
            {
                'id': movie.id,
                'title': movie.title,

            }
            for movie in movies
        ]

        response_data = {
            'count': len(serialized_data),
            'results': serialized_data,
        }

        return JsonResponse(response_data)

#Viewing movie details including showtimes
class MovieDetails(View):
    def get(self, request):
        movies = Movie.objects.all()

        #each dictionary represents one movie
        serialized_data = [
            {
                'id': movie.id,
                'title': movie.title,
                'description': movie.description,
                'showtimes': movie.showtimes,

            }
            for movie in movies
        ]

        response_data = {
            'count': len(serialized_data),
            'results': serialized_data,
        }

        return JsonResponse(response_data)

#Booking a seat for a specific showtime
class BookingSeat(View):
    def get(self, request):
        movies = Movie.objects.all()
        bookings = Booking.objects.all()

        #each dictionary represents one movie
        serialized_data = [
            {
                'id': movie.id,
                'title': movie.title,
                'description': movie.description,
                'showtimes': movie.showtimes,

            }
            for movie in movies
        ]

        response_data = {
            'count': len(serialized_data),
            'results': serialized_data,
        }

        return JsonResponse(response_data)

#Viewing user booking history
class BookingHistory(View):
    def get(self, request):
        bookings = Booking.objects.all()

        #each dictionary represents one movie
        serialized_data = [
            {
                'id': booking.id,
                'user': booking.title,
                'movie': booking.description,
                'seat_number': booking.showtimes,

            }
            for booking in bookings
        ]

        response_data = {
            'count': len(serialized_data),
            'results': serialized_data,
        }

        return JsonResponse(response_data)