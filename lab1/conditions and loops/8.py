a=input("enter the number ")
temp=int(a)
rev=a[::-1]

if temp==int(rev):
    print(f'the number is the plindrome')
else:
    print("the number is non palindrome")
