class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks  # Dictionary: {subject: marks}

    def average(self):
        return sum(self.marks.values()) / len(self.marks)

    def has_failed(self):
        return any(mark < 40 for mark in self.marks.values())

    def __str__(self):
        return f"Name: {self.name}, Roll: {self.roll}, Marks: {self.marks}, Avg: {self.average():.2f}"


students = []


def add_student():
    name = input("Enter student name: ")
    roll = input("Enter roll number: ")
    subjects = input("Enter subjects (comma-separated): ").split(",")
    marks = {}
    for sub in subjects:
        sub = sub.strip()
        marks[sub] = int(input(f"Enter marks for {sub}: "))
    students.append(Student(name, roll, marks))
    print("Student added successfully.\n")


def view_all():
    if not students:
        print("No records found.\n")
    for s in students:
        print(s)
    print()


def show_topper():
    if not students:
        print("No student records.\n")
        return
    max_avg = max(s.average() for s in students)
    toppers = [s for s in students if s.average() == max_avg]
    print("Topper(s):")
    for s in toppers:
        print(s)
    print()


def search_by_roll():
    roll = input("Enter roll number to search: ")
    found = False
    for s in students:
        if s.roll == roll:
            print(s)
            found = True
            break
    if not found:
        print("Student not found.\n")


def show_failed_students():
    failed = [s for s in students if s.has_failed()]
    if not failed:
        print("No failed students.\n")
    else:
        print("Students who failed in one or more subjects:")
        for s in failed:
            print(s)
    print()


def update_marks():
    roll = input("Enter roll number to update marks: ")
    for s in students:
        if s.roll == roll:
            for sub in s.marks:
                new_mark = int(input(f"Enter new marks for {sub} (current: {s.marks[sub]}): "))
                s.marks[sub] = new_mark
            print("Marks updated.\n")
            return
    print("Student not found.\n")


def menu():
    while True:
        print("------ Student Report Card Management ------")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Display Topper(s)")
        print("4. Search by Roll Number")
        print("5. Show Failed Students")
        print("6. Update Marks")
        print("7. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_student()
        elif choice == "2":
            view_all()
        elif choice == "3":
            show_topper()
        elif choice == "4":
            search_by_roll()
        elif choice == "5":
            show_failed_students()
        elif choice == "6":
            update_marks()
        elif choice == "7":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


menu()
