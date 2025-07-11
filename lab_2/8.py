a = []
c = []
f = []
for i in range(1, 49):
    a.append(i)
u = set(a)
print("Enter the roll numbers who play cricket: ")
i = 0
while True:
    x = int(input(f"Enter {i+1} roll number: "))
    c.append(x)
    i += 1
    ch = input("Any one else?(y/n)").lower()
    if ch != 'y':
        break
print("Enter the roll numbers who play football: ")
i = 0
while True:
    x = int(input(f"Enter {i+1} roll number: "))
    f.append(x)
    i += 1
    ch = input("Any one else?(y/n)").lower()
    if ch != 'y':
        break
c_set = set(c)
f_set = set(f)
int_set = c_set & f_set
union_set = c_set | f_set
set1 = c_set.difference(int_set)
set2 = f_set.difference(int_set)
neither = u.difference(union_set)
print(f"{int_set} play both cricket and football")
print(f"{set1} play cricket only")
print(f"{set2} play football only")
print(f"{neither} play neither of the sports")