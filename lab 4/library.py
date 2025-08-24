
dit={}
def add_contact():
    name=input("enter the name : ")
    phone=input("Enter the phoen number : ")
    with open("contacts.txt" ,'a') as f:
        f.write(f'{name},{phone}\n')
def data_reading():
    dit.clear()
    with open('contacts.txt','r') as f:
        contant=f.readlines()
        for line in contant:
            
            name,phone=line.strip().split(',')
            dit[name]=phone   
def search_contacts():
    data_reading()
    contact=input('Enter the contact : ')
    for name in dit.keys():
        if name==contact:
            print(f'name:{name} phone:{dit[name]}')  

def show_all_contact():
    data_reading()
    for name,phone in dit.items():
        print(f"name : {name}  {phone}")
 
def num():   
    while True:
        print("\n===== Contact Book =====")
        print("1. Add New Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            show_all_contact()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")
        
num()