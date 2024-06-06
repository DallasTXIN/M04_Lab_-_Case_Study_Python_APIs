#Dallas Lawson
#M04 Lab - Case Study: Python APIs
#This is to make sure that every book is labeled via everything listed down in the code.
#The code is similar to the code I used for M03 Lab - Case Study: Lists, Functions, and Classes

class Book():
    def __init__(self, id, book_name, author, publisher):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher

class LongBook(Book):
     def __init__(self, id, book_name, author, publisher):
        super().__init__(id, book_name, author, publisher)

OwnerOfBook = LongBook("1", "IT", "Stephen King", "Viking")
print("The ID of the book is:", OwnerOfBook.id)
print("The name of the book is:", OwnerOfBook.book_name)
print("The author of the book is:", OwnerOfBook.author)
print("The publisher of the book is:", OwnerOfBook.publisher)