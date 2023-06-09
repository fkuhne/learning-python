# Python Object Oriented Programming by Joe Marini course example
# Using class-level and static methods


class Book:
    # TODO: Properties defined at the class level are shared by all instances
    # different from the instance attributes because they are shared at the class level
    BOOK_TYPES = ("HARDCOVER", "PAPERBACK", "EBOOK")

    # TODO: double-underscore properties are hidden from other classes
    __booklist = None

    # TODO: create a class method
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES

    # TODO: create a static method
    @staticmethod
    def getbooklist():
        if Book.__booklist == None:
            Book.__booklist = []    
        return Book.__booklist
    

    # instance methods receive a specific object instance as an argument
    # and operate on data specific to that object instance
    def setTitle(self, newtitle):
        self.title = newtitle

    # when a class is created this function is called. it is an initializer,
    # not a constructor.
    def __init__(self, title, booktype):
        self.title = title
        print('Title is ' + self.title)
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type.")
        else:
            self.booktype = booktype

# TODO: access the class attribute
print("Book types: ", Book.getbooktypes())

# TODO: Create some book instances
b1 = Book("Brave New World", "HARDCOVER")
b2 = Book("War and Peace", "PAPERBACK")

print(b1)
print(b1.title)

# TODO: Use the static method to access a singleton object
thebooks = Book.getbooklist()
print(thebooks)
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
