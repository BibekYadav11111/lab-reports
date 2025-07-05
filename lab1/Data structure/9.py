first=[1,2,3,4,5,6,7,8,9]
second=[4,6,7,87,8,9,]
onlyfirst=[i for i in first if i not in second]
print(onlyfirst)