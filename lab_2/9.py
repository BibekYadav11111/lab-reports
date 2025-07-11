import random
c = set(random.sample(range(1, 100), 5))
print(f"The original set of random numbers is: {c}")
c_list = list(c)
while len(c_list) < 10:
    x = int(input(f"Enter number #{len(c_list)+1}: "))
    if x not in c_list:
        c_list.append(x)
    else:
        print("Duplicate! Enter a unique number.")
final_set = set(c_list)
print(f"\nThe new set is: {final_set}")
print(f"The maximum number in the above set is: {max(final_set)}")
print(f"The minimum number in the above set is: {min(final_set)}")