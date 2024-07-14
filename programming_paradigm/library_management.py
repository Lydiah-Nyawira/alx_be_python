class Book:
    def __init__(self,title, author):
        self.title = title
        self.author = author
        self.is_checked_out = False

    def check_out(self):
        self.is_checked_out = True
    
    def return_book(self):
        self.is_checked_out = False
              
    def _is_checked_out(self):
        return self.is_checked_out          

class Library:
    def __init__(self):
        self._books = []

    def add_book(self,book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title and not book._is_checked_out():
                book.check_out()
                return True
        return False    
    
    def return_book(self, title):
        for book in self._books:
            if book.title == title and book._is_checked_out():
                book.return_book()
                return True
        return False  

    def list_available_books(self):
        available_books = [book.title for book in self._books if not book._is_checked_out()]
        if available_books:
            print("\n".join(available_books))
        else:
            print("No available books.")    