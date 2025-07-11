def input_student_data():
    d = {}
    n = int(input("How many students? "))
    for i in range(n):
        name = input(f"\nEnter the name of student {i+1}: ")
        marks = []
        print(f"Enter the marks in three subjects of {name}:")
        for j in range(1, 4):
            mark = int(input(f"Mark {j}: "))
            marks.append(mark)
        d[name] = marks
    return d

def calculate_averages(d):
    new = {}
    for key in d:
        avg = round(sum(d[key]) / 3, 2)
        new[key] = avg
    return new

def display_averages(new):
    print("\nAverage marks of each student:")
    for student, avg in new.items():
        print(f"{student}: {avg}")

def find_topper(new):
    topper = max(new, key=lambda k: new[k])
    print(f"\nStudent with highest average is: {topper}")
    print(f"Their average is: {new[topper]:.2f}")

def update_marks(d, new):
    update = input("\nDo you want to update marks of any student? (y/n): ").lower()
    while update == 'y':
        student = input("Enter the name of the student whose marks you want to update: ")
        if student in d:
            print(f"Current marks for {student}: {d[student]}")
            new_marks = []
            print("Enter the new marks for three subjects:")
            for i in range(1, 4):
                mark = int(input(f"Mark {i}: "))
                new_marks.append(mark)
            d[student] = new_marks
            avg = round(sum(new_marks) / 3, 2)
            new[student] = avg
            print(f"Marks and average updated for {student}!")
        else:
            print("Student not found.")
        update = input("\nDo you want to update marks of another student? (y/n): ").lower()

def main():
    d = input_student_data()
    new = calculate_averages(d)
    display_averages(new)
    update_marks(d, new)
    print("\nUpdated marks dictionary:")
    print(d)
    print("\nUpdated averages dictionary:")
    print(new)
    sorted_new = dict(sorted(new.items(), key=lambda item: item[1]))
    print("\nStudents sorted by average marks:")
    print(sorted_new)
    find_topper(new)

main()