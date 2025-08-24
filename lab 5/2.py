# 2. Create a class Student with attributes name and marks. Create three objects
# of the class and display their details using a method show_details().
class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def show_details(self):
        print(f'name : {self.name} marks : {self.marks}')
s1=Student('anish','34')
s2=Student('Bandhan','32')
s3=Student('bibiek','45')
s1.show_details()
s2.show_details()
s3.show_details()
        