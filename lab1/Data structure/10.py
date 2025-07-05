new_dict={}
d=int(input("enter how many times you want to enter the data : "))
for i in range(d):
    key=input("enter the key you want to set : ")
    value=input("enter the value you want to set : ")
    new_dict[key]=value
print("do you want to search for the data : ")
chose=input('enter "yes" to continue and "no" for discotinue to search the items : ')
if chose.lower()=='yes':
    key=input("enter the key")
    print(new_dict[key])