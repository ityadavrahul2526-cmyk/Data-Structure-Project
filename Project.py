import tkinter as tk
from tkinter import messagebox

def add_book():
    book_id = id_entry.get()
    book_name = name_entry.get()
    author = author_entry.get()

    if book_id and book_name and author:
        books.insert(tk.END, f"{book_id} | {book_name} | {author}")

        id_entry.delete(0, tk.END)
        name_entry.delete(0, tk.END)
        author_entry.delete(0, tk.END)

        messagebox.showinfo("Success",
                            "Your book has been added successfully!")
    else:
        messagebox.showwarning("Warning",
                               "Please enter all details.")

def delete_book():
    selected = books.curselection()

    if selected:
        books.delete(selected)
        messagebox.showinfo("Success",
                            "Your selected book has been deleted!")
    else:
        messagebox.showwarning("Warning",
                               "Please select a book first.")

root = tk.Tk()
root.title("Library Book Record")
root.geometry("500x500")
root.configure(bg="#DCEEFF")

# Black outer border
frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="solid",
    highlightbackground="black",
    highlightthickness=2
)

frame.pack(padx=5, pady=5)

tk.Label(frame, text="LIBRARY BOOK RECORD",
         font=("Arial", 18, "bold"),
         bg="#154360", fg="white").pack(fill="x", pady=10)

tk.Label(frame, text="Book ID",
         font=("Arial", 11, "bold"),
         bg="white", fg="#154360").pack(pady=(10, 2))

id_entry = tk.Entry(frame, width=35, bd=2, relief="sunken")
id_entry.pack()

tk.Label(frame, text="Book Name",
         font=("Arial", 11, "bold"),
         bg="white", fg="#154360").pack(pady=(12, 2))

name_entry = tk.Entry(frame, width=35, bd=2, relief="sunken")
name_entry.pack()

tk.Label(frame, text="Author Name",
         font=("Arial", 11, "bold"),
         bg="white", fg="#154360").pack(pady=(12, 2))

author_entry = tk.Entry(frame, width=35, bd=2, relief="sunken")
author_entry.pack()

tk.Button(frame, text="Add Book",
          command=add_book,
          width=15,
          bg="#3498DB",
          fg="white",
          font=("Arial", 10, "bold")).pack(pady=15)

tk.Label(frame, text="Book Records",
         font=("Arial", 11, "bold"),
         bg="white", fg="#154360").pack()

books = tk.Listbox(frame,
                    width=50,
                    height=8,
                    bd=3,
                    relief="sunken")
books.pack(pady=8)

tk.Button(frame, text="Delete Book",
          command=delete_book,
          width=15,
          bg="#E74C3C",
          fg="white",
          font=("Arial", 10, "bold")).pack(pady=10)

root.mainloop()
