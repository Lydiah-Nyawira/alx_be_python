class Book:
    def __init__(self, title, author):
        self.title = title(str)
        self.author = author(str)

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title,author)
        self.file_size = file_size

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count =page_count

class Library:
    def __init__(self):
        self.books = [] 

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            if isinstance(book, Book):
                print(f"{self.title} by Jane {self.author}")
            if isinstance(book,EBook):
                print(f"{self.title} by {self.author}, {self.file_size}:")
            if isinstance(book, PrintBook):
                print(f"{self.title} by {self.author}, {self.page_count}:")                               