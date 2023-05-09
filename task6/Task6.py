import numpy as np

# p1


def diagonal_nines():
    x = np.eye(3) * 9
    return x


# p2
def bool_indexing():
    arr = np.arange(2, 33, 2)
    arr = arr.reshape(4, 4)
    mean = np.mean(arr)
    std = round(np.std(arr), 2)
    std1 = mean - 0.5*std
    std2 = mean + 0.5*std
    x = std1 < arr
    l = arr < std2
    j = x == l
    half_std = arr[j]
    # print(half_std)
    return arr , half_std 


# p3
def zero_arr():
    arr = np.zeros((9, 9), dtype=int)
    return arr


# p4
def broadcasting():
    arr = np.ones((4, 4), dtype=int)
    arr1 = np.array([[1, 2, 3, 4]])
    arr2 = arr1 * arr
    return arr2

