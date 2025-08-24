# Create a base class Animal with a method speak() that prints "Animal makes
# a sound". Derive a class Dog from Animal and override the speak() method
# to print "Dog barks". Instantiate the Dog class and call its speak() method.
class Animal:
    def speak(self):
        print("animal makes sound ")

class dog(Animal):
    def speak(self):
        print("dog bark")
d=dog()
d.speak()