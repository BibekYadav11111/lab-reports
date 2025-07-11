a = [1, 3, 2, 4, 5, 6, 7, 8, 9, 10]
new_list = []
for i in range(len(a)):
    if i % 2 == 0:
        new_list.append(a[i])
for num in a:
    if num < 2:
        continue
    prime = True
    for j in range(2, int(num ** 0.5) + 1):
        if num % j == 0:
            prime = False
            break
    if prime and num not in new_list:
        new_list.append(num)
new_list.sort()
print("Original List:", a)
print("New List:", new_list)