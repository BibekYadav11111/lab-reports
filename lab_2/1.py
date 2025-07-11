nums = []
n = int(input("Enter how many numbers: "))
for i in range(n):
    num = int(input(f"Enter number {i + 1}: "))
    nums.append(num)

print("\nOriginal List:", nums)

print("\n--- Using Built-in Functions ---")
print("Maximum:", max(nums))
print("Minimum:", min(nums))
sorted_builtin = sorted(nums)
print("Sorted List:", sorted_builtin)
unique_builtin = list(set(nums))
unique_builtin.sort()
print("List without duplicates:", unique_builtin)

print("\n--- Without Using Built-in Functions ---")
max_num = nums[0]
min_num = nums[0]
for num in nums:
    if num > max_num:
        max_num = num
    if num < min_num:
        min_num = num
print("Maximum:", max_num)
print("Minimum:", min_num)
sorted_custom = nums.copy()
for i in range(len(sorted_custom)):
    for j in range(0, len(sorted_custom) - i - 1):
        if sorted_custom[j] > sorted_custom[j + 1]:
            sorted_custom[j], sorted_custom[j + 1] = sorted_custom[j + 1], sorted_custom[j]
print("Sorted List:", sorted_custom)
unique_custom = []
for num in sorted_custom:
    if num not in unique_custom:
        unique_custom.append(num)
print("List without duplicates:", unique_custom)