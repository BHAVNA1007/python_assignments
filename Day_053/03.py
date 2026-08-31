'''
QUESTION 3: LIBRARY BOOK RECORD ANALYSIS(3 marks)

A library wants to maintain and analyze its book records using NamedTuple.

Each book contains the following information:

Fields:
book_id, title, author, price

Requirements:
Read N book records from the user and store them in a list of NamedTuple.
Display all book details.
Find and display the most expensive book.
Find and display the cheapest book.
Calculate and display the average price of all books.
Display all books whose price is greater than the average book price.
Test Case

Input:

Enter number of books: 6

Enter details for Book 1:
Enter Book ID: B201
Enter Title: C Programming
Enter Author: Robert
Enter Price: 400

Enter details for Book 2:
Enter Book ID: B202
Enter Title: Web Development
Enter Author: Martin
Enter Price: 650

Enter details for Book 3:
Enter Book ID: B203
Enter Title: Python Advanced
Enter Author: Robert
Enter Price: 800

Enter details for Book 4:
Enter Book ID: B204
Enter Title: Database Systems
Enter Author: Thomas
Enter Price: 500

Enter details for Book 5:
Enter Book ID: B205
Enter Title: Machine Learning
Enter Author: David
Enter Price: 900

Enter details for Book 6:
Enter Book ID: B206
Enter Title: Computer Networks
Enter Author: Martin
Enter Price: 350
Expected Output
All Book Details:
B201 C Programming Robert 400
B202 Web Development Martin 650
B203 Python Advanced Robert 800
B204 Database Systems Thomas 500
B205 Machine Learning David 900
B206 Computer Networks Martin 350

Most Expensive Book:
B205 Machine Learning David 900

Cheapest Book:
B206 Computer Networks Martin 350

Average Book Price:
600.0

Books With Price Greater Than Average:
B202 Web Development Martin 650
B203 Python Advanced Robert 800
B205 Machine Learning David 900
'''

from collections import namedtuple

n = int(input("Number of books: "))

Book = namedtuple('Book', ['book_id', 'title', 'author', 'price'])

library = []

# Read book records
for i in range(n):

    print(f"\nEnter details for Book {i + 1}:")

    bid = input("Enter Book ID: ")
    ttl = input("Enter Title: ")
    auth = input("Enter Author: ")
    p = int(input("Enter Price: "))

    library.append(Book(bid, ttl, auth, p))


# Display all book details
print("\nAll Book Details:")

for b in library:
    print(b.book_id, b.title, b.author, b.price)


# Find most expensive book
costly_book = library[0]

for i in range(1, len(library)):
    if costly_book.price < library[i].price:
        costly_book = library[i]

print("\nMost Expensive Book:")
print(costly_book.book_id, costly_book.title, costly_book.author, costly_book.price)


# Find cheapest book
cheap_book = library[0]

for i in range(1, len(library)):
    if cheap_book.price > library[i].price:
        cheap_book = library[i]

print("\nCheapest Book:")
print(cheap_book.book_id, cheap_book.title, cheap_book.author, cheap_book.price)


# Calculate average price
total = 0

for b in library:
    total += b.price

average = total / len(library)

print("\nAverage Book Price:")
print(average)


# Books whose price is greater than average
print("\nBooks With Price Greater Than Average:")

for b in library:
    if b.price > average:
        print(b.book_id, b.title, b.author, b.price)