dict1={
    'a':10,'b':20,'c':30
}
dict2={
    'b':30,'c':45,'d':89
}
mergedict={**dict1,**dict2}

for key in dict1:
    if key in dict2:
        mergedict[key]=dict1[key]+dict2[key]
print(mergedict)

a=False
if a:
    print("it is true")
else:
    print("false")