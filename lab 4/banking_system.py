# Create a simple banking system that:
# ● Stores customer info in a file
# ● Allows deposits and withdrawals using functions
# ● Updates customer balance
# ● Logs all transactions in a separate file
# ● Handles exceptions gracefully
# Files Used:
# customers.txt — stores customer records in the format:
# Name,AccountNumber,Balance
# transactions.txt — appends every deposit or withdrawal record with timestamp
import datetime

d={}
def transcation(action,ammount):
    timestamp=datetime.datetime.now()
    with open('transcation.txt','a') as f:
        f.write(f"{timestamp},{action},{ammount}\n")
def save_changes():
    with open('customers.txt','w') as f:
        for acnum,data in d.items():
            f.write(f'{data[0]},{acnum},{data[1]}\n')

def add_account():
    name=input("Enter the name : ")
    acnum=input("Enter the account number : ")
    balance=0
    with open('customers.txt','a') as f:
        f.write(f"{name},{acnum},{balance}\n")
        print("Account was created succesfully ! ")
def data_reading():
    d.clear()
    try:
        with open('customers.txt','r') as f:
            contant=f.readlines()
            for line in contant:
                name,acnum,balance=line.strip().split(',')
                d[acnum]=[name,float(balance)]
    except FileNotFoundError:
        open('customers.txt','w').close

def deposite():
    user=input('Enter the counsotmer account number : ')
    balance=float(input("Enter the ammount : "))
    data_reading()
    if user in d:
        for ac in d.keys():
            if ac==user:
                d[ac][1]=d[ac][1]+balance
                print(f"balance = {balance}")
    transcation("deposite",balance)
    save_changes()

def withdraw():
    user=input('Enter the counsotmer account number : ')
    balance=float(input("Enter the ammount : "))
    data_reading()
    if user in d:
        for ac in d.keys():
            if ac==user:
                if d[ac][1]>balance:
                    d[ac][1]=d[ac][1]-balance
                    print(f"balance = {d[ac][1]}")
                else:
                    print('Insufficinet funds ! ')
    transcation("withdraw",balance)
    save_changes()
    
def update_balance():
    user=input('Enter the counsotmer account number : ')
    balance=float(input("Enter the ammount : "))
    data_reading()
    for ac in d.keys():
        if ac==user:
            d[ac][1]=d[ac][1]+balance
            print(f"balance = {balance}")
    transcation("updatbalance",balance)

def show_all_customers():
    data_reading()
    for keys,data in d.items():
        print(f"account no : {keys} name : {data[0]} balance : {data[1]}")
def show_all_tarnscation():
    try:
        with open('transcation.txt','r') as f:
            content=f.readlines()
            for line in content:
                timestampe,action,amount=line.strip().split(',')
                print(f"{timestampe},{action},{amount}")
    except FileNotFoundError:
        open("transcation.txt",'w').close()
def search_account():
    data_reading()
    account=input("Enter the account number : ")
    for key,data in d.items():
        if key==account:
            print(f'account no : {key} name : {data[0]} balance {data[1]}')

def menu():
    while True:
        print("\n===== Banking System =====")
        print("1. Add New Account")
        print("2. View All Customers")
        print("3. Search Account")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Update balance")
        print("7. show all the transation")
        print("8. Exite")

        choice = input("Enter your choice (1-8): ")

        if choice == '1':
            add_account()
        elif choice == '2':
            show_all_customers()
        elif choice == '3':
            search_account()
        elif choice == '4':
            deposite()
        elif choice == '5':
            withdraw()
        elif choice=='6':
            update_balance()
        elif choice=='7':
            show_all_tarnscation()
        elif choice == '8':
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

menu()