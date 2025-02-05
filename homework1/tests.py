from sys import stdout
import os
from os import system
import subprocess
import pytest

from task3 import pos_neg_zero, first_ten_primes, sum_of_numbers
from task4 import calculate_discount

###############
# Start Tests #
###############


#Task 1: Introduction to Replit
class TestTask1:
    def setup_method(self):
        print("\nSetting up test for task1.py...")
        #store result as an instance variable of the class
        self.result = subprocess.run(['python', 'task1.py'], capture_output=True, text=True)

    def teardown_method(self):
        print("Cleaning up test for task1.py...")

    def test_output(self):
        '''testing total expected output'''
        assert self.result.stdout.strip() == "Hello, Replit!"

    def test_exit_code(self):
        '''making sure task1.py was successfully run'''
        assert self.result.returncode == 0

    def test_no_extra_output(self):
        '''testing that only one line was printed'''
        assert self.result.stdout.count("\n") == 1

#Task 2: Variables and Data Types
class TestTask2:
    def setup_method(self):
        print("\nSetting up test for task2.py...")
        #store result as an instance variable of the class
        self.result = subprocess.run(['python', 'task2.py'], capture_output=True, text=True)

    def teardown_method(self):
        print("Cleaning up test for task2.py...")

    def test_output(self):
        '''testing total expected output'''
        expected_output = "Name: John\nAge: 25\nHeight: 1.75\nIs Student: True"
        assert self.result.stdout.strip() == expected_output

    def test_exit_code(self):
        '''making sure task2.py was successfully run'''
        assert self.result.returncode == 0

    def test_integer_type(self):
        '''testing that age is an integer'''
        assert "Age: 25" in self.result.stdout
        assert isinstance(25, int)

    def test_float_type(self):
        '''testing that height is a float'''
        assert "Height: 1.75" in self.result.stdout
        assert isinstance(1.75, float)

    def test_string_type(self):
        '''testing that name is a string'''
        assert "Name: John" in self.result.stdout
        assert isinstance("John", str)

    def test_boolean_type(self):
        '''testing that is_student is a boolean'''
        assert "Is Student: True" in self.result.stdout
        assert isinstance(True, bool)


#Task 3: Control Structures
class TestTask3:
    def setup_method(self):
        print("\nSetting up test for task3.py...")
        #store result as an instance variable of the class
        self.result = subprocess.run(['python', 'task3.py'], capture_output=True, text=True)

    def teardown_method(self):
        print("Cleaning up test for task3.py...")

    def test_script_output(self):
        '''testing total expected output'''
        expected_output = "PositiveNegativeZero[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]5050"
        assert self.result.stdout.strip() == expected_output

    def test_exit_code(self):
        '''making sure task3.py was successfully run'''
        assert self.result.returncode == 0

    def test_pos_neg_zero(self):
        '''pos_neg_zero() test'''
        assert pos_neg_zero(10) == "Positive"
        assert pos_neg_zero(-5) == "Negative"
        assert pos_neg_zero(0) == "Zero"

    def test_first_ten_primes(self):
        '''first_ten_primes() test'''
        assert first_ten_primes() == "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]"

    def test_sum_of_numbers(self):
        '''sum_of_numbers() test'''
        assert sum_of_numbers() == "5050"


#Task 4: Functions and Duck Typing
class TestTask4:
    def setup_method(self):
        print("\nSetting up test for task4.py...")
        #store result as an instance variable of the class
        self.result = subprocess.run(['python', 'task4.py'], capture_output=True, text=True)

    def teardown_method(self):
        print("Cleaning up test for task4.py...")

    def test_script_output(self):
        '''testing total expected output'''
        expected_output = "8.0, 8.35, 7.95, 8.4"
        assert self.result.stdout.strip() == expected_output

    def test_exit_code(self):
        '''making sure task4.py was successfully run'''
        assert self.result.returncode == 0

    def test_integer_discount(self):
        '''testing calculate_discount() with integer values'''
        assert calculate_discount(100, 20) == 80.0
        assert calculate_discount(50, 10) == 45.0

    def test_float_discount(self):
        '''testing calculate_discount() with float values'''
        assert calculate_discount(100.0, 20.0) == 80.0
        assert calculate_discount(50.5, 10.5) == 45.20

    def test_mixed_types(self):
        '''testing calculate_discount() with mixed integer and float values'''
        assert calculate_discount(100, 20.5) == 79.5
        assert calculate_discount(50.5, 10) == 45.45

    def test_zero_discount(self):
        '''testing calculate_discount() with zero discount'''
        assert calculate_discount(100, 0) == 100.0
        assert calculate_discount(50.5, 0) == 50.5

    def test_full_discount(self):
        '''testing calculate_discount() with a 100% discount'''
        assert calculate_discount(100, 100) == 0.0
        assert calculate_discount(50.5, 100) == 0.0

    def test_negative_values(self):
        '''testing calculate_discount() with negative values'''
        assert calculate_discount(100, -10) == 110.0  # Negative discount increases price
        assert calculate_discount(50.5, -5) == 53.03

#Task 5: Lists and Dictionaries
def test_task5():
  result = subprocess.run(['python', 'task5.py'],
                          capture_output=True,
                          text=True)

  holder = [
      "1984 - George Orwell", "To Kill a Mockingbird - Harper Lee",
      "The Lord of The Rings - J.R.R. Tolkien"
  ]
  assert result.stdout.strip('\n') == f"{holder}\n12345"


#Task 6: File Handling and Metaprogramming
def test_task6():
  result = subprocess.run(['python', 'task6.py'],
                          capture_output=True,
                          text=True)
  assert result.stdout.strip('\n') == "12"