# 1. Create a class Book with attributes title, author, and price. Write a
# constructor to initialize these values and create an object with sample data.
# ● Add a method display_info() to the Book class that prints the book's
# title, author, and price. Call this method using a Book object.
# ● Add a method update_price(new_price) to the Book class that updates
# the book's price. Demonstrate how to use it with an object.
class Book:
    def __init__(self,title,author,price):
        self.title=title
        self.author=author
        self.price=price
    def display_info(self):
        print(f"title : {self.title} author : {self.author} price : {self.price}")
    def update_price(self,new_price):
        self.price=new_price
b=Book("harry",'JK',2100)
b.display_info()
b.update_price(34)
b.display_info()