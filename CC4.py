import tkinter as tk

class LibraryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Library Management System")
        
        self.books = []
        
        self.title_label = tk.Label(root, text="Library Management System", font=("Helvetica", 16))
        self.title_label.pack()

        self.book_title_label = tk.Label(root, text="Book Title:")
        self.book_title_label.pack()

        self.book_title_entry = tk.Entry(root)
        self.book_title_entry.pack()

        self.add_button = tk.Button(root, text="Add Book", command=self.add_book)
        self.add_button.pack()

        self.view_button = tk.Button(root, text="View Books", command=self.view_books)
        self.view_button.pack()

        self.delete_button = tk.Button(root, text="Delete Book", command=self.delete_book)
        self.delete_button.pack()

        self.output_text = tk.Text(root, height=5, width=40, font=("Helvetica", 12))
        self.output_text.pack()

    def add_book(self):
        book_title = self.book_title_entry.get()
        if book_title:
            self.books.append(book_title)
            self.book_title_entry.delete(0, tk.END)
            self.output_text.insert(tk.END, f"Book '{book_title}' added successfully.\n")
        else:
            self.output_text.insert(tk.END, "Please enter a book title.\n")

    def view_books(self):
        if self.books:
            books_list = "\n".join(self.books)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "Books in Library :\n")
            self.output_text.insert(tk.END, books_list)
        else:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, "There are no books in the library.\n")

    def delete_book(self):
        book_title = self.book_title_entry.get()
        if book_title in self.books:
            self.books.remove(book_title)
            self.book_title_entry.delete(0, tk.END)
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Book '{book_title}' deleted successfully.\n")
        else:
            self.output_text.delete("1.0", tk.END)
            self.output_text.insert(tk.END, f"Book '{book_title}' not found in the library.\n")

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryManagementApp(root)
    root.mainloop()
