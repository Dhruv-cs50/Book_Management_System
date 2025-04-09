# Book Manager Application

## Overview
The Book Manager Application is a desktop software built with Python, featuring a graphical user interface (GUI) developed using Tkinter and backed by a SQLite database managed through SQLAlchemy ORM. It enables users to perform CRUD operations (Create, Read, Update, Delete) on book records.

## Project Structure
```
book_manager/
├── database.py
├── gui.py
├── books.db
└── README.md
```

## Requirements
- Python 3.x
- Tkinter (usually bundled with Python)
- SQLAlchemy

## Installation
1. **Clone or download the repository:**
   ```bash
   git clone <https://github.com/Dhruv-cs50/Book_Management_System/tree/main>
   ```

2. **Navigate to the project directory:**
   ```bash
   cd book_manager
   ```

3. **Install SQLAlchemy:**
   ```bash
   pip install sqlalchemy
   ```

## Usage
Run the application:

```bash
python gui.py
```

## Features

- **Add Book:** Insert a new book into the database.
- **View Books:** Display all book records stored in the database.
- **Update Book:** Modify existing book records using their unique ID.
- **Delete Book:** Remove book records from the database.

## Database Structure

The SQLite database (`books.db`) contains a table named `books`:

| Column | Data Type |
|--------|-----------|
| id     | Integer (Primary Key) |
| title  | String    |
| author | String    |
| year   | Integer   |
| price  | Float     |

## Files Explained

### `database.py`
Handles all database interactions, including establishing connections and performing CRUD operations using SQLAlchemy.

### `gui.py`
Manages the graphical user interface, providing a user-friendly interface to interact with the database operations defined in `database.py`.

## Contributing
Contributions are welcome. Please create an issue or submit a pull request.

## License
This project is open-source and free to use and modify.


