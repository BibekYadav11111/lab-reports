# 5. Define a class Person with attributes name and age. Derive a class Employee
# from Person with additional attributes employee_id and salary. Implement a
# method display_employee() in Employee that prints all the details. Create an
# instance of Employee and display the information.
class person:
    def __init__(self,employ_id,salary):
        self.employ_id=employ_id
        self.salary=salary
    def display_employ(self):
        print(f"employ_id : {self.employ_id} salary : {self.salary}")
    
p1=person(1234,40000)
p1.display_employ()