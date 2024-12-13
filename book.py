import datetime
import random

class Book:
    def __init__(self, title, authors, publishing_year, price, quantity, isbn=None, date_added=None, date_updated=None):
        self.title = title
        self.authors = authors
        self.isbn = isbn if isbn else random.randint(1000000000, 9999999999)
        self.publishing_year = publishing_year
        self.price = price
        self.quantity = quantity
        self.date_added = date_added if date_added else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.date_updated = date_updated if date_updated else datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            'Title': self.title,
            'Authors': self.authors,
            'ISBN': self.isbn,
            'Publishing Year': self.publishing_year,
            'Price': self.price,
            'Quantity': self.quantity,
            'Date Added': self.date_added,
            'Date Updated': self.date_updated
        }
