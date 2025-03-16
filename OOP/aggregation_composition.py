# Aggregation: A relationship where one object(whole e.g. library) contains references to one or more independent objects(parts e.g. books). The classes can exist without each other
# Composition: Composed object directly owns its components which cannot exist independently

print(__name__)

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        return [book.title for book in self.books]
        

class Book:
    def __init__(self, title, author):
        self.title = title 
        self.author = author 
        
library = Library("sjpl")
book1 = Book('my book1', 'pnm')
book2 = Book('my book2', 'lkm')
book3 = Book('my book3', 'jnm')

library.add_book(book1)
print(library.list_books())