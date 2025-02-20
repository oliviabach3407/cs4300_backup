from rest_framework import serializers
from .models import Movie, Seat, Bookings

'''
https://www.geeksforgeeks.org/serializers-django-rest-framework/
General Syntax:
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['user_id', 'account_name', 'user', 'created']
'''

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = '__all__'

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = '__all__'
