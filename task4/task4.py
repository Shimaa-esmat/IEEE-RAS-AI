import math
lst = input("Enter list separated by space ").split(" ")
lst = list(map(int, lst))
lst = sorted(lst)
print(lst)
mean = 0
for i in lst:
    mean += i
mean /= len(lst)
print(f"mean = {round(mean,2)}")
l = math.floor(len(lst)/2)
if len(lst) % 2 != 0:
    median = lst[l]
    print(f"median = {median}")
else:
    median = (lst[l]+lst[l-1])/2
    print(f"median = {median}")
lst2 = []
for i in lst:
    lst2.append(lst.count(i))
m = max(lst2)
if m > 1:
    mode = lst[lst2.index(m)]
else:
    mode = median
print(f"mode = {mode}")
