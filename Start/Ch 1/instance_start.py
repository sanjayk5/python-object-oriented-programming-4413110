# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, price, pages, type):
        self.title = title
        # TODO: add properties
        self.price = price
        self.pages = pages
        self.type = type
        self.__limited_edition = "limited edition available"

    # TODO: create instance methods
    def set_discount(self, discount):
        self._discount = discount

    def get_price(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price


# TODO: create some book instances
b1 = Book("War and Peace", 25, 1050, "Paperback")
b2 = Book("The Catcher in the Rye", 50, 250, "Hardbound")

# TODO: print the price of book1
print(b1.price)

# TODO: try setting the discount
print(b2.get_price())
b2.set_discount(0.3)
print(b2.get_price())

# TODO: properties with double underscores are hidden by the interpreter
print(b2._discount)
# print(b2.__limited_edition)
print(b2._Book__limited_edition)
