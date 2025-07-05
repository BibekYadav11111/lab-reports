names=['bandhan','anup','bibek','abhay','anish','bandhan','bibek']
names_count={}

for name in names:
    if name in names_count:
        names_count[name]+=1
    else:
        names_count[name]=1
print(names_count)