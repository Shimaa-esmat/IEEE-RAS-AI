# task2 p4

def remove():
    lst = input('Enter elements of a list separated by space ').split(" ")
    lst = list(map(str, lst))
    for i in lst:
        count = lst.count(i)
        if count > 1:
            lst.remove(i)
    print(lst)
# remove()

# p1


def counteven():
    while True:
        try:
            a = input(
                "enter the list element seperated by space :").split(" ")
            a = list(map(int, a))
            return len(list(filter(lambda x: (x % 2 == 0), a)))
        except Exception as ex:
            print("you enter wrong value")
# print(counteven())

# p2


def index1():
    while True:
        try:

            lst = input(
                "enter the list element seperated by space :").split(" ")
            lst = list(map(int, lst))
            n = int(input("Enter number : "))
            if n in lst:
                # return lst.index(n)
                print("index", lst.index(n))
            else:
                lst.sort()
                for i in lst:
                    if n > i:
                        x = lst.index(i)+1
                # return lst, x
                print("sorted", lst, "index", x)

        except Exception as ex:
            print("you enter wrong value")
# index1()

# p3


def closesttarget():
    lst = input("enter the list element seperated by space :").split(" ")
    lst = list(map(int, lst))
    n = int(input("Enter number : "))
    lst.sort()
    for l in lst:
        for k in lst:
            for j in lst:
                for i in lst:
                    sum = i + j + k + l
                    if sum <= n:
                        if j != i and k != i and i != l and j != k and j != l and k != l:
                            x = i
                            c = j
                            v = k
                            b = l
    print(x, c, v, b)
# closesttarget()

# p4

# with open(r"C:\\Users\ASD\Downloads\dummy_grades.txt", 'r') as f:
#     d = {}
#     for i in range(20):
#         text = f.readline()
#         words = text.split()
#         d[i] = words

#     for i in range(9):
#         if d[i][2] == 'N/A':
#             print("line", i+1)
#             print(d[i][2])
#         for j in range(9):
#             if d[i][4] < d[j][4]:
#                 x = i+1
#     print(x)
#     n = 0
#     v = {}
#     for i in range(9):
#         if d[i][2] != 'N/A':
#             # print(i)
#             v = int(d[i][2])
#             # print(v)
#             n += v
#             s = i

#     n /= (s+1)
#     print(n)
#     for l in range(9):
#         for j in range(9):
#             if d[i][2] > d[j][2]:
#                 m = i
#     print(d[m][6])
