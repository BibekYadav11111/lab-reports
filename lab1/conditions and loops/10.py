while True:
    num1=int(input("Enter the first number : "))
    num2=int(input("Enter the second number : "))
    chose=input("Enter the operation you like to have eg:( +,*,-,/) : ")
    while True:
        if chose=='+':
            print(num1+num2)
            break
        elif chose=='-':
            print(num1-num2)
            break
        elif chose=='*':
            print(num1*num2)
            break
        elif chose=='/':
            print(num1/num2)
            break
        else :
            print("Enter the valid arthemitic symbol")
    con=input('enter y to continue')
    if con!='y':
        break