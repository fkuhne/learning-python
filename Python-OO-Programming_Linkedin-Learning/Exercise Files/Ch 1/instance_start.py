# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        # these ones are called INSTANCE ATTRIBUTES bc they belong to the 
        # instance being declared.
        self.author = author
        self.pages = pages
        self.price = price

        self.__secret = "This is a secret attribute"

    # TODO: create instance methods
    def getprice(self):
        # note that the _discount attribute is not created for every instance of the
        # class. so we have to test for its presence before using it.
        if hasattr(self, "_discount"):
            return self.price - self.price*self._discount
        return self.price
    
    def setdiscount(self, amount):
        # the underscore in the beggining of the attribute name means that this
        # attribute should not be used publicly.
        self._discount = amount


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.getprice())

# TODO: try setting the discount
print(b2.getprice())
b2.setdiscount(0.25)
print(b2.getprice())


# TODO: properties with double underscores are hidden by the interpreter
# print(b2.__secret)
print(b2._Book__secret)
