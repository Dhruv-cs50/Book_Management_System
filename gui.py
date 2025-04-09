# gui.py

import tkinter as tk
from tkinter import ttk, messagebox
import database

# Main Application Window
root = tk.Tk()
root.title("Book Manager Application")
root.geometry("700x500")

# Labels and Entry fields
tk.Label(root, text="Book ID").grid(row=0, column=0, padx=10, pady=5)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Title").grid(row=1, column=0, padx=10, pady=5)
entry_title = tk.Entry(root)
entry_title.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Author").grid(row=2, column=0, padx=10, pady=5)
entry_author = tk.Entry(root)
entry_author.grid(row=2, column=1, padx=10, pady=5)

tk.Label(root, text="Year").grid(row=3, column=0, padx=10, pady=5)
entry_year = tk.Entry(root)
entry_year.grid(row=3, column=1, padx=10, pady=5)

tk.Label(root, text="Price").grid(row=4, column=0, padx=10, pady=5)
entry_price = tk.Entry(root)
entry_price.grid(row=4, column=1, padx=10, pady=5)

# Treeview for displaying books
tree = ttk.Treeview(root, columns=("ID", "Title", "Author", "Year", "Price"), show='headings')
tree.heading("ID", text="ID")
tree.heading("Title", text="Title")
tree.heading("Author", text="Author")
tree.heading("Year", text="Year")
tree.heading("Price", text="Price")
tree.grid(row=6, column=0, columnspan=4, pady=20, padx=10, sticky='nsew')

# Functions for button actions
def add_book():
    try:
        book_id = int(entry_id.get())
        if database.add_book(book_id, entry_title.get(), entry_author.get(), int(entry_year.get()), float(entry_price.get())):
            messagebox.showinfo("Success", "Book added successfully!")
        else:
            messagebox.showwarning("Error", "Book with this ID already exists.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")
    display_books()

def display_books():
    for row in tree.get_children():
        tree.delete(row)
    for book in database.get_all_books():
        tree.insert('', 'end', values=(book.id, book.title, book.author, book.year, book.price))

def update_book():
    try:
        book_id = int(entry_id.get())
        if database.update_book(book_id, entry_title.get(), entry_author.get(), int(entry_year.get()), float(entry_price.get())):
            messagebox.showinfo("Success", "Book updated successfully!")
        else:
            messagebox.showwarning("Error", "Book ID does not exist.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")
    display_books()

def delete_book():
    try:
        book_id = int(entry_id.get())
        if database.delete_book(book_id):
            messagebox.showinfo("Success", "Book deleted successfully!")
        else:
            messagebox.showwarning("Error", "Book ID does not exist.")
    except ValueError:
        messagebox.showerror("Error", "Invalid input!")
    display_books()

# Buttons
tk.Button(root, text="Add Book", command=add_book).grid(row=5, column=0, pady=5)
tk.Button(root, text="Display Books", command=display_books).grid(row=5, column=1, pady=5)
tk.Button(root, text="Update Book", command=update_book).grid(row=5, column=2, pady=5)
tk.Button(root, text="Delete Book", command=delete_book).grid(row=5, column=3, pady=5)

# Start the GUI event loop
display_books()
root.mainloop()
