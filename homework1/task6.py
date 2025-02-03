'''
Write a Python program in Replit that reads a text file (you can create a sample text file) and counts the number of words in it.
Implement metaprogramming techniques to dynamically generate function names for your pytest test cases based on the filenames of the text files.
Include pytest test cases that verify the word count for each text file.
'''


def count_words_in_file(filename):
  with open(filename, 'r') as file:
    text = file.read()
    words = text.split()
    return len(words)


print(count_words_in_file("task6.txt"))