'''3. You are building a Library Management System. Create a `Book` class with properties like `title`, 
`author`, and `isbn`. Write a method to display book details.'''

class Book:
    def __init__(self,title,author,isbn):
        self.title=title
        self.author=author
        self.isbn=isbn

    def display(self):
        print(f"The title of the book is {self.title}")
        print(f"The author of the book is {self.author}")
        print(f"The isbn number of the book is {self.isbn}")


book=Book("How to Code","Hima","123")
book.display()

        

