'''
Create a list in Replit of your favorite books, including book titles and authors.
Use list slicing to print the first three books in the list.
Create a dictionary that represents a basic student database, including student names and their corresponding student IDs.
Implement pytest test cases to verify the correctness of your code for each data structure.
'''
#a list of favorite books (book title - name of author)
favorite_books = [
    "1984 - George Orwell",
    "To Kill a Mockingbird - Harper Lee",
    "The Lord of The Rings - J.R.R. Tolkien",
    "The Day of The Jackal - Frederick Forsyth",
]

#print the first three books in the list
print(favorite_books[:3])

#a dictionary of students (name: number)
student_database = {
    "John": "12345",
    "Jane": "67890",
    "Bob": "54321",
    "Alice": "98765",
}

#print the value associated with the key "John"
print(student_database["John"])
