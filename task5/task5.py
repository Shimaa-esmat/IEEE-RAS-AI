import math
lst = input("Enter list separated by space ").split(" ")
lst = list(map(int, lst))
lst = sorted(lst)
print(lst)
print(f"max = {max(lst)}")

l = math.floor(len(lst)/2)

if len(lst) % 2 != 0:
    Q2 = lst[l]
else:
    Q2 = (lst[l]+lst[l-1])/2

lst2 = []
lst3 = []
for i in lst:
    if i < Q2:
        lst2.append(i)
    if i > Q2:
        lst3.append(i)
M = math.floor(len(lst2)/2)
if len(lst2) % 2 != 0:
    Q1 = lst2[M]
else:
    Q1 = (lst2[M]+lst2[M-1])/2

print(f"Q1 = {Q1}")

print(f"Q2 = {Q2}")

s = math.floor(len(lst3)/2)
if len(lst3) % 2 != 0:
    Q3 = lst3[s]
else:
    Q3 = (lst3[s]+lst3[s-1])/2
print(f"Q3 = {Q3}")

print(f"min = {min(lst)}")
print(f"range = {max(lst)-min(lst)}")
print(f"IQR = {Q3-Q1}")

N = 0
for i in lst:
    N += i
N /= len(lst)
print(N)
v = 0
for i in lst:
    k = round(i - N, 2)
    v += pow(k, 2)
v /= len(lst)

print(f"Variance = {round(v,2)}")
print(f"Standard deviation = {round(math.sqrt(v),2)}")
