# Create a base class Shape with a method area(). Derive two classes
# Rectangle and Circle from Shape. Implement the area() method in both
# derived classes. Instantiate Rectangle and Circle, and demonstrate
# polymorphism by calling their area() methods.

class Shape :
    def area(self):
        raise NotImplementedError("Sub class is requried")
class Rectangle(Shape):
    def __init__(self,length,breath):
        self.length=length
        self.breath=breath
    def area(self):
        return self.length*self.breath
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        return 3.14*((self.radius)**(2))
shapes=[Rectangle(3,4),Circle(7)]
for ar in shapes:
    print(f" Area : {ar.area()}")
        
