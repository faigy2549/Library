# Library Management System

Welcome to the Library Management System project! This project is built using Python and utilizes SQLite3 for the database. The system supports both admin and user roles, each with distinct features and capabilities. This README file will guide you through the setup, usage, and features of the project.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Introduction

The Library Management System is designed to manage the operations of a library. It allows administrators to manage books, users, and borrowing records, while regular users can search for books, borrow and return them, and view their borrowing history.

## Features

### Admin Features
- **User Management**: Add, edit, and delete user accounts.
- **Book Management**: Add, edit, and delete book records.
- **Borrowing Management**: View, approve, or reject borrowing requests.
- **Return Management**: Record the return of borrowed books.

### User Features
- **User Registration**: Register for a new account.
- **Book Search**: Search for books by title, author, or genre.
- **Book Borrowing**: Request to borrow available books.
- **Book Returning**: Return borrowed books.
- **Borrowing History**: View personal borrowing history and status of current borrowings.

## Requirements

- Python 3.8 or higher
- SQLite3 (comes pre-installed with Python)
- PyCharm IDE (optional, but recommended for development)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/yourusername/library-management-system.git
   cd library-management-system
Set up a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
Install the dependencies:

pip install -r requirements.txt
Initialize the database:

python init_db.py
Run the application:

python app.py
Open your web browser and navigate to:

http://127.0.0.1:5000/
Usage
Admin Login:

Use the admin credentials to log in and access the admin dashboard.
User Registration:

New users can register by clicking on the registration link on the login page.
Book Search and Borrowing:

Users can search for books and request to borrow them if available.
Borrowing Management:

Admins can view and manage borrowing requests and returns.

Enjoy managing your library with ease! If you have any questions or run into any issues, please open an issue on the GitHub repository. Happy managing!
