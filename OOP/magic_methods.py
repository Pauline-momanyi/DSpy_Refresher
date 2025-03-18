# Also known as dunder (double under methods)e.g __init__, __name__. Automatically called by built in operations

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author 
        self.pages = pages 
    #if you print the created book, you get the location in memory. Now we want to customize the result
    def __str__(self): #return string rep of the object
        return f"{self.title} by {self.author}"
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __add__(self, other):
        return self.pages + other.pages
    
    def __getitem__(self, key):
        if key == 'title':
            return self.title 
        elif key == 'author':
            return self.author
        else:
            return self.pages
        
book1 = Book("Test", "Popo", 260) #used the dunder to initialize 
book2 = Book("Test1", "Popo1", 50)

print(book1)
print(book1 < book2)
print(book1+book2)
print(book1['title']) #using __getitem__