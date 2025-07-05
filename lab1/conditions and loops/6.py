num_list=[]
for i in range(10):
    p=int(input("Enter the number"))
    num_list.append(p)
positive=[]
nega=[]
zero=[]
for i in range(len(num_list)):
    if num_list[i]>0:
        positive.append(num_list[i])
    elif num_list[i]==0:
        zero.append(num_list[i])
    else:
        nega.append(num_list[i])
        
print(f" positive = {len(positive)} \n nega = {len(nega)} zero = {len(zero)}")
