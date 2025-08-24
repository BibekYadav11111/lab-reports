class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Address:
    def __init__(self, street, city, zipcode):
        self.street = street
        self.city = city
        self.zipcode = zipcode

class Contact:
    def __init__(self, person, address):
        self.person = person
        self.address = address

    def display_contact(self):
        print(f"Name: {self.person.name}")
        print(f"Age: {self.person.age}")
        print(f"Street: {self.address.street}")
        print(f"City: {self.address.city}")
        print(f"Zipcode: {self.address.zipcode}")

person = Person("bandhan", 28)
address = Address("mainapokhar", "bardiya", "90923")

contact = Contact(person, address)

contact.display_contact()
