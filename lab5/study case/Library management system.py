# Case Study: Library Management System

# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def borrow(self):
        if self.available:
            self.available = False
            print(f"The book '{self.title}' by {self.author} has been borrowed.")
        else:
            print(f"Sorry, the book '{self.title}' is currently not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"The book '{self.title}' by {self.author} has been returned.")
        else:
            print(f"The book '{self.title}' by {self.author}' is already available in the library.")

# Define the Library class
class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"The book '{book.title}' by {book.author} has been added to the library.")

    def display_available_books(self):
        available_books = [book for book in self.books if book.available]
        if available_books:
            print("Available books in the library:")
            for book in available_books:
                print(f"'{book.title}' by {book.author}")
        else:
            print("No books available in the library.")

# Create Book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("1984", "George Orwell")

# Create Library object
library = Library()

# Add books to the library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
print()
# Display available books
library.display_available_books()
print()
# Borrow a book
book1.borrow()
print()
# Display available books after borrowing
library.display_available_books()
print()
# Return a book
book1.return_book()
print()
# Display available books after returning
library.display_available_books()