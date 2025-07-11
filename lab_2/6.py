a = []
a_t = ()
sum = 0
d = {}
max_count = 0
mode = []
n = int(input("Enter the value of n: "))
for i in range(1, n + 1):
    a.append(int(input(f"Enter {i} number: ")))
a_t = tuple(a)
for num in a_t:
    sum += num
avg = sum / n
print(avg)
for i in range(len(a)):
    for j in range(0, len(a) - i - 1):
        if a[j] > a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp
if n % 2 == 1:
    median = a[n // 2]
else:
    mid1 = a[n // 2 - 1]
    mid2 = a[n // 2]
    median = (mid1 + mid2) / 2
print(median)
for i in a_t:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
for key in d:
    if d[key] > max_count:
        max_count = d[key]
for key in d:
    if d[key] == max_count:
        mode.append(key)
print(f"The mode/modes of this tuple = {mode}")