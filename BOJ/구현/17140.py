from sys import stdin
from copy import deepcopy

std = stdin.readline
r, c, k = map(int, std().split())
r, c = r-1, c-1
A = []

for i in range(3):
    A.append(list(map(int, std().split())))

row, column = 3, 3


def sort_op(arr):
    global row
    arr = list(filter(lambda x: x != 0, arr))
    set_arr = list(set(arr))
    tuple_arr = []
    count_arr = {key: 0 for key in set_arr}
    for a in arr:
        count_arr[a] += 1

    for a in set_arr:
        tuple_arr.append((a, count_arr[a]))
    tuple_arr = sorted(tuple_arr, key=lambda x: (x[1], x[0]))
    sort_arr = []
    c = 0
    for t in tuple_arr:
        if c == 50:
            break
        sort_arr.append(t[0])
        sort_arr.append(t[1])
        c += 1

    return sort_arr


def R_op():
    global column
    new_arr = []
    for a in A:
        arr = sort_op(a)
        new_arr.append(arr)
        if len(arr) > column:
            column = len(arr)
    for i in range(len(new_arr)):
        for j in range(column - len(new_arr[i])):
            new_arr[i].append(0)
    return new_arr


def C_op():
    global row, column
    c_arr = [[] for i in range(column)]
    new_arr = []
    for i in range(row):
        for j in range(column):
            c_arr[j].append(A[i][j])

    for i in range(len(c_arr)):
        arr = sort_op(c_arr[i])
        new_arr.append(arr)
        if len(arr) > row:
            row = len(arr)

    for i in range(len(new_arr)):
        for j in range(row - len(new_arr[i])):
            new_arr[i].append(0)
    sort_arr = [[0 for i in range(column)] for j in range(row)]
    for i in range(column):
        for j in range(row):
            sort_arr[j][i] = new_arr[i][j]

    return sort_arr


time = 101
answer = -1
if r < row and c < column and A[r][c] == k:
    answer = 0
if answer != 0:
    for i in range(1, time):
        if row >= column:
            A = deepcopy(R_op())
        else:
            A = deepcopy(C_op())
        if r < row and c < column and A[r][c] == k:
            answer = i
            break
    print(answer)
else:
    print(answer)
