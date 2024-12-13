import json
from book import Book
import datetime

class Library:
    def __init__(self):
        self.books = []
        self.lend_records = []
        self.load_books()
        self.load_lend_records()

    def load_books(self):
        try:
            with open('books.json', 'r') as file:
                books_data = json.load(file)
                for book_data in books_data:
                    book = Book(
                        title=book_data['Title'],
                        authors=book_data['Authors'],
                        publishing_year=book_data['Publishing Year'],
                        price=book_data['Price'],
                        quantity=book_data['Quantity'],
                        isbn=book_data['ISBN'],
                        date_added=book_data['Date Added'],
                        date_updated=book_data['Date Updated']
                    )
                    self.books.append(book)
        except FileNotFoundError:
            print("No existing books found. Starting a new library.")
        except json.JSONDecodeError:
            print("Error decoding the JSON file.")

    def save_books(self):
        with open('books.json', 'w') as file:
            json.dump([book.to_dict() for book in self.books], file, indent=4)

    def load_lend_records(self):
        try:
            with open('lend_records.json', 'r') as file:
                self.lend_records = json.load(file)
        except FileNotFoundError:
            print("No existing lend records found.")
        except json.JSONDecodeError:
            print("Error decoding the JSON file.")

    def save_lend_records(self):
        with open('lend_records.json', 'w') as file:
            json.dump(self.lend_records, file, indent=4)

    def add_book(self, title, authors, publishing_year, price, quantity):
        try:
            price = float(price)
            quantity = int(quantity)
            if quantity < 0:
                raise ValueError("Quantity cannot be negative.")
        except ValueError as e:
            print(f"Error: {e}")
            return
        
        book = Book(title, authors, publishing_year, price, quantity)
        self.books.append(book)
        self.save_books()
        print(f"Book '{title}' added successfully.")

    def view_books(self):
        self.books.sort(key=lambda x: x.title)  # Sort books by title
        for book in self.books:
            print(f"Title: {book.title}, Authors: {book.authors}, ISBN: {book.isbn}, Year: {book.publishing_year}, Price: {book.price}, Quantity: {book.quantity}")

    def update_book(self, isbn, title=None, authors=None, publishing_year=None, price=None, quantity=None):
        for book in self.books:
            if book.isbn == isbn:
                if title:
                    book.title = title
                if authors:
                    book.authors = authors
                if publishing_year:
                    book.publishing_year = publishing_year
                if price:
                    try:
                        book.price = float(price)
                    except ValueError:
                        print("Invalid price format.")
                        return
                if quantity:
                    try:
                        book.quantity = int(quantity)
                        if book.quantity < 0:
                            raise ValueError("Quantity cannot be negative.")
                    except ValueError:
                        print("Invalid quantity format.")
                        return
                book.date_updated = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                self.save_books()
                print(f"Book with ISBN '{isbn}' updated successfully.")
                return
        print(f"No book found with ISBN '{isbn}'.")

    def delete_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]
        self.save_books()
        print(f"Book with ISBN '{isbn}' deleted successfully.")

    def lend_book(self, title, borrower_name, borrower_phone):
        for book in self.books:
            if book.title == title and book.quantity > 0:
                book.quantity -= 1
                due_date = (datetime.datetime.now() + datetime.timedelta(days=14)).strftime("%Y-%m-%d %H:%M:%S")
                lend_record = {
                    'Borrower Name': borrower_name,
                    'Borrower Phone': borrower_phone,
                    'Book Title': title,
                    'Due Date': due_date
                }
                self.lend_records.append(lend_record)
                self.save_books()
                self.save_lend_records()
                print(f"Book '{title}' lent to {borrower_name}. Due on {due_date}.")
                return
        print(f"There are not enough books available to lend '{title}'.")

    def return_book(self, title, borrower_name):
        for record in self.lend_records:
            if record['Book Title'] == title and record['Borrower Name'] == borrower_name:
                self.lend_records.remove(record)
                self.save_lend_records()
                for book in self.books:
                    if book.title == title:
                        book.quantity += 1
                        self.save_books()
                        print(f"Book '{title}' returned by {borrower_name}.")
                        return
        print(f"No record found for '{title}' borrowed by {borrower_name}.")
