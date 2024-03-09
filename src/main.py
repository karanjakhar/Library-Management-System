from book import Book
from storage import Storage
from user import User
from check import Checkout
from logger import Logger

class LibraryManagementSystem:
    def __init__(self):
        self.books = []
        self.users = []
        self.checkouts = []
        self.logger = Logger()

    def add_book(self, title, author, isbn, copies=1):
        book = Book(title, author, isbn, copies)
        self.books.append(book)
        self._save_books()
        self.logger.log(f"Added book: {book}")
        print("Book added.")

    def update_book(self, isbn, title=None, author=None, copies=None):
        book = self.find_book(isbn)
        if book:
            old_book = Book(book.title, book.author, book.isbn, book.copies)
            book.update(title, author, isbn, copies)
            self._save_books()
            self.logger.log(f"Updated book: {old_book} -> {book}")
        else:
            print("Book not found.")

    def delete_book(self, isbn):
        book = self.find_book(isbn)
        if book:
            self.books.remove(book)
            self._save_books()
            self.logger.log(f"Deleted book: {book}")
            print("Book deleted.")
        else:
            print("Book not found.")

    def list_books(self):
        for book in self.books:
            print(book)

    def add_user(self, name, user_id):
        user = User(name, user_id)
        self.users.append(user)
        self._save_users()
        self.logger.log(f"Added user: {user}")
        print("User added.")

    def update_user(self, user_id, name=None):
        user = self.find_user(user_id)
        if user:
            old_user = User(user.name, user.user_id)
            user.name = name
            self._save_users()
            self.logger.log(f"Updated user: {old_user} -> {user}")
            print("User updated.")
        else:
            print("User not found.")

    def delete_user(self, user_id):
        user = self.find_user(user_id)
        if user:
            self.users.remove(user)
            self._save_users()
            self.logger.log(f"Deleted user: {user}")
            print("User deleted.")
        else:
            print("User not found.")
    def list_users(self):
        for user in self.users:
            print(user)

    def checkout_book(self, user_id, isbn):
        book = self.find_book(isbn)
        user = self.find_user(user_id)
        if not book:
            print("Book not found.")
            return
        if not user:
            print("User not found.")
            return
        if book.copies <= 0:
            print("No copies available for checkout.")
            return
        book.copies -= 1
        checkout = Checkout(user_id, isbn)
        self.checkouts.append(checkout)
        self._save_checkouts()
        self.logger.log(f"Checked out book: {book} by {user}")
        print("Book checked out.")

    def checkin_book(self, user_id, isbn):
        checkout = self.find_checkout(user_id, isbn)
        if not checkout:
            print("No checkout record found.")
            return
        book = self.find_book(isbn)
        if not book:
            print("Book not found.")
            return
        book.copies += 1
        self.checkouts.remove(checkout)
        self._save_checkouts()
        self.logger.log(f"Checked in book: {book}")
        print("Book checked in.")

    def list_checkouts(self):
        for checkout in self.checkouts:
            print(f"User: {checkout.user_id}, ISBN: {checkout.isbn}")

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def find_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    def find_checkout(self, user_id, isbn):
        for checkout in self.checkouts:
            if checkout.user_id == user_id and checkout.isbn == isbn:
                return checkout
        return None

    def _save_books(self):
        Storage.save_books(self.books, '../data/books.json')

    def _save_users(self):
        Storage.save_books(self.users, '../data/users.json')

    def _save_checkouts(self):
        Storage.save_books([checkout.__dict__ for checkout in self.checkouts], '../data/checkouts.json')

    def main_menu(self):
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Update Book")
        print("3. Delete Book")
        print("4. List Books")
        print("5. Add User")
        print("6. Update User")
        print("7. Delete User")
        print("8. List Users")
        print("9. Checkout Book")
        print("10. Checkin Book")
        print("11. List Checkouts")
        print("12. Exit")
        choice = input("Enter choice: ")
        return choice

    def main(self):
        while True:
            choice = self.main_menu()
            if choice == '1':
                title = input("Enter title: ")
                author = input("Enter author: ")
                isbn = input("Enter ISBN: ")
                copies = int(input("Enter number of copies: "))
                self.add_book(title, author, isbn, copies)
                
            elif choice == '2':
                isbn = input("Enter ISBN of the book to update: ")
                title = input("Enter new title (leave blank to keep current): ")
                author = input("Enter new author (leave blank to keep current): ")
                copies = int(input("Enter new number of copies (leave blank to keep current): ") or 0)
                self.update_book(isbn, title, author, copies)
                
            elif choice == '3':
                isbn = input("Enter ISBN of the book to delete: ")
                self.delete_book(isbn)
                
            elif choice == '4':
                self.list_books()
            elif choice == '5':
                name = input("Enter user name: ")
                user_id = input("Enter user ID: ")
                self.add_user(name, user_id)
                
            elif choice == '6':
                user_id = input("Enter user ID of the user to update: ")
                name = input("Enter new name (leave blank to keep current): ")
                self.update_user(user_id, name)
                
            elif choice == '7':
                user_id = input("Enter user ID of the user to delete: ")
                self.delete_user(user_id)
                
            elif choice == '8':
                self.list_users()
            elif choice == '9':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkout: ")
                self.checkout_book(user_id, isbn)
                
            elif choice == '10':
                user_id = input("Enter user ID: ")
                isbn = input("Enter ISBN of the book to checkin: ")
                self.checkin_book(user_id, isbn)
                
            elif choice == '11':
                self.list_checkouts()
            elif choice == '12':
                print("Exiting.")
                break
            else:
                print("Invalid choice, please try again.")

if __name__ == "__main__":
    lms = LibraryManagementSystem()
    lms.main()