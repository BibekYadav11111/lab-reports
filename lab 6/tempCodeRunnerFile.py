class Book:
    def __init__(self,title,author):
        self.author=author
        self.title=title
    def __str__(self):
        return f"{self.title} by {self.author}"
b=Book('Harry potter ','J.K Rowling')
print(b)