# Movie Theater Booking App

This is a simple movie theater booking app that allows users to:

* View available movies
* Login/Sign-in and Logout
* Book a ticket for a movie by picking a seat and a date
* View their booking history (tickets they booked in the past)

## Project Structure

There is a main project file movie_theater_bookings with two subdirectories:

* The main project directory: movie_theater_bookings/movie_theater_bookings/
* The main app directory: movie_theater_bookings/bookings/

![image](https://github.com/user-attachments/assets/0c281428-3e01-4de1-8b7a-8628f7bb0900)

There is also a templates/bookings/ folder for all HTML templates related to the app.
And there is a static folder that holds the styles.css sheet for the entire app.

![image](https://github.com/user-attachments/assets/916c1bf0-d49c-4954-8008-156beecc60d2)

## How to Run this Project Locally

### Dependencies

* Python on my computer (the path)
* Python3

### Packages Installed With Pip

* virtualenv
* django-bootstrap5
* djangorestframework 
* coverage

### On DevEdu - INSTRUCTIONS FOR RUNNING ON DEVEDU

* Open the terminal and 'cd' to \cs4300\obach2\homework2\movie_theater_booking
* run: ```source myenv/bin/activate```
* run ```python3 manage.py runserver```

### On My Local Machine:

**Disclaimer** - this doesn't work on your local machine because the path to my 
python executable was used to create the virtual environment. 

These are the instructions that **I** use locally:

* Open the terminal and 'cd' to C:\Users\olivi\Desktop\Programming\Advanced\cs4300\homework2\movie_theater_booking
* run: ```myenv\Scripts\Activate``` --> this activates the virtual machine
* run: ```python manage.py runserver``` --> this runs the server (THIS IS THE COMMAND THAT DOESN'T WORK BECAUSE IT'S LOOKING FOR PYTHON ON MY MACHINE)
* Navigate to 127.0.0.1:8000 or whatever IP is listed in the terminal

### How to Run the Tests:

After having followed the instructions above to activate the virtual machine:

* run: ```python manage.py test``` --> there are 17 tests that should run

I also installed coverage to see the coverage of my tests:

* run: ```coverage run --source='.' manage.py test``` --> runs the tests with coverage in mind
* run: ```coverage report -m``` --> view the coverage report
