import tkinter as tk
from tkinter import filedialog, messagebox

class Book:
    def __init__(self, title, year, author, genres):
        self.title = title
        self.year = year
        self.author = author
        self.genres = genres

class Author:
    def __init__(self, name, biography, books):
        self.name = name
        self.biography = biography
        self.books = books



class LibraryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Library App")

        self.books = self.load_books_from_file("books.txt")
        self.authors = self.load_authors_from_file("authors.txt")

        self.menu_label = tk.Label(master, text="Choose a Feature:", width=30, bd=2, bg="#C6E2FF")
        self.menu_label.pack()

        self.show_books_button = tk.Button(master, text="Show Books", command=self.show_books, width=30, bd=2, bg="#00b7cb")
        self.show_books_button.pack()

        self.show_authors_button = tk.Button(master, text="Show Authors", command=self.show_authors, width=30, bd=2, bg="#00b7cb")
        self.show_authors_button.pack()


    def load_books_from_file(self, file_name):
        books = []
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    book = Book(data[0], data[1], data[2], data[3:])
                    books.append(book)
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"The file {file_name} was not found.")
        return books

    def load_authors_from_file(self, file_name):
        authors = []
        try:
            with open(file_name, 'r') as file:
                for line in file:
                    data = line.strip().split(',')
                    author = Author(data[0], data[1], data[2:])
                    authors.append(author)
        except FileNotFoundError:
            messagebox.showerror("File Not Found", f"The file {file_name} was not found.")
        return authors


    def show_books(self):
        book_names = [book.title for book in self.books]
        chosen_book = self.choose_from_list("Choose a Book", book_names)
        if chosen_book:
            book_info = f"Title: {chosen_book.title}\nYear: {chosen_book.year}\nAuthor: {chosen_book.author}\nGenres: {', '.join(chosen_book.genres)}"
            messagebox.showinfo("Book Information", book_info)

    def show_authors(self):
        author_names = [author.name for author in self.authors]
        chosen_author = self.choose_from_list("Choose an Author", author_names)
        if chosen_author:
            author_info = f"Author: {chosen_author.name}\nBiography: {chosen_author.biography}\nBooks Written: {', '.join(chosen_author.books)}"
            messagebox.showinfo("Author Information", author_info)


    def choose_from_list(self, title, options):
        chosen_option = tk.simpledialog.askstring(title, f"Choose one:\n{', '.join(options)}")
        if chosen_option:
            index = options.index(chosen_option)
            return self.books[index] if title == "Choose a Book" else self.authors[index]
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()