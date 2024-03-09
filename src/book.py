class Book:
    def __init__(self, title, author, isbn, copies=1):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.copies = copies

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}) - Copies: {self.copies}"

    def update(self, title=None, author=None, isbn=None, copies=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if isbn:
            self.isbn = isbn
        if copies is not None:
            self.copies = copies