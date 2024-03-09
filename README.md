# Library Management System

This is a Python-based Library Management System (LMS) that allows users to manage books, users, and checkouts. The system provides functionalities to add, update, delete, list, and search for books and users, check out and check in books, track book availability, and log operations.

## Design Decisions

- **Object-Oriented Design**: The system is designed using object-oriented principles, with classes representing entities like Book, User, and Checkout. This design promotes code reusability, maintainability, and scalability.

- **Separation of Concerns**: Different functionalities are separated into classes (e.g., Book, User, Checkout, Storage) to ensure that each class has a single responsibility. This makes the code easier to understand and maintain.

- **File-Based Storage**: Data is stored in JSON files (books.json, users.json, checkouts.json) to ensure reliable storage and retrieval of information.

- **Logging**: A Logger class is used to log operations (e.g., adding books, updating users) to a log file (log.txt), providing a record of system activities.

## Architecture

The system consists of the following main components:

1. **Book**: Represents a book with attributes such as title, author, ISBN, and number of copies. Provides methods to update book information.

2. **User**: Represents a user with attributes such as name and user ID. Provides methods to update user information.

3. **Checkout**: Represents a checkout record with attributes for user ID, ISBN, checkout date, and return date.

4. **Storage**: Manages file-based storage of books, users, and checkouts. Provides methods to save and load data from JSON files.

5. **Logger**: Logs operations performed in the system to a log file.

6. **LibraryManagementSystem**: Main class that encapsulates the system's functionalities. Provides methods to interact with books, users, and checkouts, and handles user input and menu navigation.

## Usage

To use the Library Management System, follow these steps:

1. Run `main.py` in `src/` to start the system.
    Command: ```cd src/  && python main.py```
2. Choose options from the main menu to perform various operations, such as adding books, updating users, checking out books, etc.
3. The system will log all operations to the `log.txt` file.

## Classes and Methods

- **Book**: Represents a book with attributes like title, author, ISBN, and copies. Provides methods to update book information (`update`).

- **User**: Represents a user with attributes like name and user ID. Provides methods to update user information (`update`).

- **Checkout**: Represents a checkout record with attributes for user ID, ISBN, checkout date, and return date.

- **Storage**: Manages file-based storage of books, users, and checkouts. Provides methods to save and load data from JSON files.

- **Logger**: Logs operations performed in the system to a log file.

- **LibraryManagementSystem**: Main class that encapsulates the system's functionalities. Provides methods to interact with books, users, and checkouts, and handles user input and menu navigation (`add_book`, `update_book`, `delete_book`, `list_books`, `add_user`, `update_user`, `delete_user`, `list_users`, `checkout_book`, `checkin_book`, `list_checkouts`).

