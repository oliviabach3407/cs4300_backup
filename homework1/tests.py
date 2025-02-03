from sys import stdout
import os
from os import system
import subprocess
import pytest

###############
# Start Tests #
###############


#Task 1: Introduction to Replit
def test_task1():
  result = subprocess.run(['python', 'task1.py'],
                          capture_output=True,
                          text=True)
  assert result.stdout.strip('\n') == "Hello, Replit!"


#Task 2: Variables and Data Types
def test_task2():
  result = subprocess.run(['python', 'task2.py'],
                          capture_output=True,
                          text=True)
  assert result.stdout.strip(
      '\n') == "Name: John\nAge: 25\nHeight: 1.75\nIs Student: True"


#Task 3: Control Structures
def test_task3():
  result = subprocess.run(['python', 'task3.py'],
                          capture_output=True,
                          text=True)
  assert result.stdout.strip(
      '\n') == "PositiveNegativeZero[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]5050"


#Task 4: Functions and Duck Typing
def test_task4():
  result = subprocess.run(['python', 'task4.py'],
                          capture_output=True,
                          text=True)
  assert result.stdout.strip('\n') == "8.0, 8.3475, 7.95, 8.4"


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