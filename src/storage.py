import json
from book import Book
class Storage:
    @staticmethod
    def save_books(books, filename):
        with open(filename, 'w') as file:
            json.dump([book.__dict__ for book in books], file)

    @staticmethod
    def load_books(filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [Book(**book_data) for book_data in data]
        except FileNotFoundError:
            return []