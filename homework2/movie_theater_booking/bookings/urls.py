from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, SeatViewSet, BookingViewSet, UserViewSet, view_movies, book_seat, booking_history, signup

#for login/signup
from django.contrib.auth import views as auth_views

#API Endpoints:
#ex. /api/movies/
router = DefaultRouter()
router.register(r'movies', MovieViewSet)
router.register(r'seats', SeatViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),  #API Endpoints
    path('', view_movies, name='movies'),
    path('book-seat/<int:movie_id>/', book_seat, name='book_seat'),
    path('booking-history/', booking_history, name='booking_history'),

    #authentication
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', signup, name='signup'), 
]