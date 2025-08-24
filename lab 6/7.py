# Create a class Book with attributes title and author. Overload the __str__()
# method to return a string representation of the Book object in the format
# "Title by Author". Test this method by printing a Book instance.
class Book:
    def __init__(self,title,author):
        self.author=author
        self.title=title
    def __str__(self):
        return f"{self.title} by {self.author}"
b=Book('Harry potter ','J.K Rowling')
print(b)