# Define a class Student with attributes name, roll_number, and marks.
# Implement a method display_info() that prints the details of the student.
# Create an instance of Student and call the display_info() method to display
# the student's details.


class student:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def info(self):
        print(f'name : {self.name} roll no: {self.roll_number} marks : {self.marks}')
s=student('bandhanr','081bel021',23)
s.info()

        
