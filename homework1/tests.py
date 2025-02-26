from sys import stdout
import os
from os import system
import subprocess
import pytest
import numpy as np
import json

'''
import for specific function tests that are
semi-independent of total script success/failure:
'''
from task2 import get_type, name, age, height, is_student
from task3 import pos_neg_zero, first_ten_primes, sum_of_numbers
from task4 import calculate_discount
from task5 import favorite_books, student_database
from task6 import count_words_in_file
from task7 import random_calculator

'''
all of my tests follow the same general format:
-setup (where the stdoutput of the task is captured)
-teardown
-test output (testing the full string of the output/file that was printed/written to at the end of the script)
          ^^ this is a test of all functions and all datatypes in the task (testing the stdout of the script)
-test exit code (testing that the script was run without error)
-test specific functions within script (beyond what was tested by test_output)
          OR test structure of variables that were in the script (things that wouldn't have output to stdout)
'''

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
        '''testing exit code for success'''
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
        '''testing exit code for success'''
        assert self.result.returncode == 0

    def test_integer_type(self):
        '''testing that age is an integer'''
        assert get_type(age) == "<class 'int'>"

    def test_float_type(self):
        '''testing that height is a float'''
        assert get_type(height) == "<class 'float'>"

    def test_string_type(self):
        '''testing that name is a string'''
        assert get_type(name) == "<class 'str'>"

    def test_boolean_type(self):
        '''testing that is_student is a boolean'''
        assert get_type(is_student) == "<class 'bool'>"

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
        '''testing exit code for success'''
        assert self.result.returncode == 0

    def test_pos_neg_zero(self):
        '''pos_neg_zero() test'''
        assert pos_neg_zero(10) == "Positive"
        assert pos_neg_zero(-2) == "Negative"
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
        '''testing exit code for success'''
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
        assert calculate_discount(100, -10) == 110.0
        assert calculate_discount(50.5, -5) == 53.03

#Task 5: Lists and Dictionaries
class TestTask5:
    def setup_method(self):
        print("\nSetting up test for task5.py...")
        #store result as an instance variable of the class
        self.result = subprocess.run(['python', 'task5.py'], capture_output=True, text=True)

    def teardown_method(self):
        print("Cleaning up test for task5.py...")

    def test_script_output(self):
        '''testing total expected output'''
        expected_output = "['1984 - George Orwell', 'To Kill a Mockingbird - Harper Lee', 'The Lord of The Rings - J.R.R. Tolkien']\n12345"
        assert self.result.stdout.strip() == expected_output

    def test_exit_code(self):
        '''testing exit code for success'''
        assert self.result.returncode == 0

    def test_list_slicing(self):
        '''testing list slicing for first three books'''
        assert favorite_books[:3] == [
            "1984 - George Orwell",
            "To Kill a Mockingbird - Harper Lee",
            "The Lord of The Rings - J.R.R. Tolkien",
        ]

    def test_student_database(self):
        '''testing student database dictionary'''
        assert student_database["John"] == "12345"
        assert student_database["Jane"] == "67890"
        assert student_database["Bob"] == "54321"
        assert student_database["Alice"] == "98765"

#Task 6: File Handling and Metaprogramming
class TestTask6:
    def setup_class(self):
        print("\nSetting up test for task6.py...")
        #store result as an instance variable of the class
        self.result = subprocess.run(['python', 'task6.py'], capture_output=True, text=True)
    
    def teardown_class(cls):
        print("Cleaning up test for task6.py...")
    
    def test_script_output(self):
        '''testing total expected output'''
        expected_output = str(104)
        assert self.result.stdout.strip() == expected_output
    
    def test_exit_code(self):
        '''testing exit code for success'''
        assert self.result.returncode == 0
    
    #https://www.packetcoders.io/dynamically-generating-tests-with-pytest-parametrization/
    @pytest.mark.parametrize("filename,expected_count", [
        ("task6_read_me.txt", 104),
        ("task6_other.txt", 14),
        ("task6_empty.txt", 0)
    ])
    def test_word_count(self, filename, expected_count):
        '''testing word count in each file'''
        assert count_words_in_file(filename) == expected_count

#Task 7: Package Control in DevEdu
class TestTask7:
    def setup_class(self):
        print("\nSetting up test for task7.py...")
        #run the script to create the file for reading
        self.result = subprocess.run(['python', 'task7.py'], capture_output=True, text=True)
        with open("task7_output.json", "r") as f:
            #to get the list of numbers in the correct format
            self.list_of_numbers = json.load(f)

    def teardown_class(self):
        print("Cleaning up test for task7.py...")
    
    def test_script_output(self):
        '''testing total expected output'''
        mean_value = np.mean(self.list_of_numbers)
        std_dev = np.std(self.list_of_numbers)
        assert 0.45 < mean_value < 0.55, "Mean value is out of expected bounds"
        assert std_dev > 0, "Standard deviation should be greater than 0"
    
    def test_exit_code(self):
        '''testing exit code for success'''
        assert self.result.returncode == 0
    
    #https://www.packetcoders.io/dynamically-generating-tests-with-pytest-parametrization/
    #if you choose a small number like 10 for the num_iterations, this test will fail
    #because there aren't enough numbers to cause the right mean and standard deviation
    @pytest.mark.parametrize("name,num_iterations", [
        ("RandomTest0-", 1000000),
        ("RandomTest0-", 100),
        ("RandomTest0-", 1000)
    ])
    def test_if_list_of_numbers_is_random(self, name, num_iterations):
        '''testing randomness within different amounts of iterations'''
        result = random_calculator(num_iterations)
        mean_value = np.mean(result)
        std_dev = np.std(result)
        assert 0.45 < mean_value < 0.55, "Mean value is out of expected bounds"
        assert std_dev > 0, "Standard deviation should be greater than 0"

