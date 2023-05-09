
with open(r"C:\\Users\ASD\Downloads\dummy_grades.txt", 'r') as f:
    d = {}
    for i in range(9):
        text = f.readline()
        words = text.split()
        d[i] = words

    for i in range(9):
        if d[i][2] == 'N/A':
            print("line", i+1)
            print(d[i][2])
        for j in range(9):
            if d[i][4] < d[j][4]:
                x = i+1
    print(x)
    n = 0
    v = {}
    for i in range(9):
        if d[i][2] != 'N/A':
            # print(i)
            v = int(d[i][2])
            # print(v)
            n += v
            s = i

    n /= (s+1)
    print(n)
    for l in range(9):
        for j in range(9):
            if d[i][2] > d[j][2]:
                m = i
    print(d[m][6])
