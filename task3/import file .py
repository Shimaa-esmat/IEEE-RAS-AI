from test import d


def import1():
    lst = list(d.values())
    # print(lst)
    fb = open("busted.txt", "w")
    for i in range(9):
        lst1 = lst[i]
        lst1.pop(6)
        lst1.pop(2)
        fb.writelines(lst1)
        fb.write(str("\n"))
    fb.close()
