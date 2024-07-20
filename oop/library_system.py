class Book:
    def __init__(self, title, author):
        self.title = title(str)
        self.author = author(str)

class EBook(Book):
    def __init__(self, file_size):
        return f"{self.title} by {self.author}, {file_size}:"

class PrintBook(Book):
    def __init__(self, page_count):
        return f"{self.title} by {self.author}, {page_count}:"

class Library:
    def __init__(self, books):
        books = [] 

    def add_book(self, book):
        self.append(Book, EBook, PrintBook)

    def list_books(self, books):
        for book in books:
            print(f"{self.title} by Jane {self.author}")                       