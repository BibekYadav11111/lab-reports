d = {}
for i in range(5):
    key = input(f"Enter the {i+1} product name: ")
    d[key] = int(input(f"Enter the price of {key}: "))
print(d)
while True:
    print("a -> Adding new products\nb -> Update the price of product\nc -> Find the product in given price range")
    choice = input("Enter your choice: ").lower()
    if choice == 'a':
        key = input("Enter the new product: ")
        if key not in d:
            d[key] = int(input(f"Enter the price of {key}: "))
        else:
            print("Product already existed.")
    elif choice == 'b':
        key = input("Enter the product to be updated: ")
        if key in d:
            d[key] = int(input(f"Enter the updated price of {key}:"))
        else:
            print("Product does not exist.")
    elif choice == 'c':
        r1 = int(input("Enter the initial value: "))
        r2 = int(input("Enter the final value: "))
        rangee = {}
        for key in d:
            if d[key] in range(r1, r2 + 1):
                rangee[key] = d[key]
        print(f"The products for your price range is/are:\n{rangee}")
    else:
        print("Invalid choice!!!")
    ch = input("Do you want to try again?").lower()
    if ch != 'y':
        break
print("Thank you for trying")