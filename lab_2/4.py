l = []
while True:
    choice = input("Enter 1 for push and 2 for pop: ")
    if choice == "1":
        num = int(input("Enter number to push: "))
        l.append(num)
    elif choice == "2":
        if len(l) == 0:
            continue
        print(f"Popped element is {l.pop()}")
    else:
        print("Invalid choice")
        break