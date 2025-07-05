s='asdfaaadd'
set1=set(s)
dict={}
for i in set1:
    dict[i]=s.count(i)
print(dict)