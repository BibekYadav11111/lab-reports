prim=[]
for num in range(50):
    non_prim=False
    if num<=1:
        non_prim=True
    for i in range(2,int(num**0.5)+1):
        if num%i==0:
            non_prim=True
            
            break
    if not non_prim:
        prim.append(num)
      
setOfprim=set(prim)
user=int(input("enter"))
if user in setOfprim:
    print('yes')
else:
    print('no')