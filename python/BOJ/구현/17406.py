from sys import stdin
from copy import deepcopy
from itertools import permutations

std = stdin.readline

R, C, K = map(int, std().split())

A, tmp = [], []
for i in range(R):
    A.append(list(map(int, std().split())))


def round(row, column, dist):
    global tmp
    for i in range(1, dist+1):
        N = 2*i+1
        start_r, start_c = row-i, column-i

        c_r, c_c = start_r, start_c
        t = tmp[c_r][c_c]
        for j in range(1, N):
            k = tmp[c_r][c_c+j]
            tmp[c_r][c_c+j] = t
            t = k

        c_r, c_c = start_r, start_c+2*i
        for j in range(1, N):
            k = tmp[c_r+j][c_c]
            tmp[c_r+j][c_c] = t
            t = k

        c_r, c_c = start_r+2*i, start_c+2*i
        for j in range(1, N):
            k = tmp[c_r][c_c-j]
            tmp[c_r][c_c - j] = t
            t = k

        c_r, c_c = start_r+2*i, start_c
        for j in range(1, N):
            k = tmp[c_r-j][c_c]
            tmp[c_r-j][c_c] = t
            t = k


change_info = []
for i in range(K):
    change_info.append(tuple(map(int, std().split())))

change_com = list(map(list, permutations(change_info, K)))

answer = 25000001

for change in change_com:
    tmp = deepcopy(A)
    for ch in change:
        r, c, s = ch
        round(r-1, c-1, s)
        # print("회전")
        # for j in range(R):
        #    print(tmp[j])
    for i in range(R):
        ans = sum(tmp[i])
        if ans < answer:
            answer = ans
if K == 0:
    for i in range(R):
        ans = sum(A[i])
        if ans < answer:
            answer = ans
    print(answer)
else:
    print(answer)
