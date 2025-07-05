num=int(input("Enter the number : "))
non_prim=False
if num<=1:
   non_prim=True
for i in range(2,int(num**0.5)+1):
    if num%i==0:
        non_prim=True
        break
if non_prim:
    print('the number is non_prim')
else:
    print('the number is prim')

