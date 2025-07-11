b = []
t = ()
n = int(input("Enter the value of n: "))
for i in range(0, n):
    a = []
    a.append(int(input(f"x{i}: ")))
    a.append(int(input(f"y{i}: ")))
    t = tuple(a)
    b.append(t)
print("Points entered:", b)
if n < 2:
    print("All points lie on a straight line.")
else:
    x0, y0 = b[0]
    x1, y1 = b[1]
    if x1 - x0 == 0:
        slope = None
    else:
        slope = (y1 - y0) / (x1 - x0)
    flag = True
    for i in range(2, n):
        x, y = b[i]
        if slope is None:
            if x != x0:
                flag = False
                break
        else:
            if (y - y0) != slope * (x - x0):
                flag = False
                break
    if flag:
        print("All points lie on a straight line.")
    else:
        print("Points do NOT lie on a straight line.")