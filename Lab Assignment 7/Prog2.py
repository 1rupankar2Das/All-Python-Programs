# Design classes for a library catalog, including books, authors, and 
# patrons. Implement methods for checking out, returning, and 
# searching for books.
class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_checked_out = False
        self.checked_out_by = None

    def __str__(self):
        return f"Book(title={self.title}, author={self.author.name}, isbn={self.isbn})"

class Author:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def __str__(self):
        return f"Author(name={self.name})"

class Patron:
    def __init__(self, name):
        self.name = name
        self.checked_out_books = []

    def check_out_book(self, book):
        if book.is_checked_out:
            print(f"Book '{book.title}' is already checked out.")
        else:
            book.is_checked_out = True
            book.checked_out_by = self
            self.checked_out_books.append(book)
            print(f"Book '{book.title}' checked out by {self.name}.")

    def return_book(self, book):
        if book in self.checked_out_books:
            book.is_checked_out = False
            book.checked_out_by = None
            self.checked_out_books.remove(book)
            print(f"Book '{book.title}' returned by {self.name}.")
        else:
            print(f"Book '{book.title}' is not checked out by {self.name}.")

    def __str__(self):
        return f"Patron(name={self.name})"

class Library:
    def __init__(self):
        self.books = []
        self.authors = []
        self.patrons = []

    def add_book(self, title, author_name, isbn):
        author = self.get_or_create_author(author_name)
        book = Book(title, author, isbn)
        author.add_book(book)
        self.books.append(book)
        print(f"Book '{title}' by {author_name} added to library.")

    def get_or_create_author(self, name):
        for author in self.authors:
            if author.name == name:
                return author
        new_author = Author(name)
        self.authors.append(new_author)
        return new_author

    def add_patron(self, name):
        patron = Patron(name)
        self.patrons.append(patron)
        print(f"Patron '{name}' added to library.")
        return patron

    def search_books_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_books_by_author(self, author_name):
        return [book for book in self.books if author_name.lower() in book.author.name.lower()]

    def check_out_book(self, isbn, patron_name):
        book = self.get_book_by_isbn(isbn)
        if book:
            patron = self.get_patron_by_name(patron_name)
            if patron:
                patron.check_out_book(book)
            else:
                print(f"No patron found with name '{patron_name}'.")
        else:
            print(f"No book found with ISBN '{isbn}'.")

    def return_book(self, isbn, patron_name):
        book = self.get_book_by_isbn(isbn)
        if book:
            patron = self.get_patron_by_name(patron_name)
            if patron:
                patron.return_book(book)
            else:
                print(f"No patron found with name '{patron_name}'.")
        else:
            print(f"No book found with ISBN '{isbn}'.")

    def get_book_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def get_patron_by_name(self, name):
        for patron in self.patrons:
            if patron.name == name:
                return patron
        return None

# Example usage
library = Library()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890")
library.add_book("To Kill a Mockingbird", "Harper Lee", "0987654321")

patron1 = library.add_patron("Alice")
patron2 = library.add_patron("Bob")

library.check_out_book("1234567890", "Alice")
library.return_book("1234567890", "Alice")

print("Books by 'Harper Lee':", library.search_books_by_author("Harper Lee"))
print("Books with 'Mockingbird' in title:", library.search_books_by_title("Mockingbird"))

