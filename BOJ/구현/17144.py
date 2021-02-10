from sys import stdin
from copy import deepcopy

std = stdin.readline
R, C, T = map(int, std().split())
m = []
for i in range(R):
    m.append(list(map(int, std().split())))

air_clean = []
for i in range(R):
    if m[i][0] == -1:
        air_clean.append(i)

nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]


def dust():
    d = deepcopy(m)
    for i in range(R):
        for j in range(C):
            if not m[i][j] in [0, -1]:
                r, c = i, j
                cnt = 0
                for k in range(4):
                    dr, dc = r+nr[k], c+nc[k]
                    if 0 <= dr < R and 0 <= dc < C and not m[dr][dc] == - 1:
                        d[dr][dc] += m[r][c] // 5
                        cnt += 1
                d[r][c] -= m[r][c]//5*cnt
    return d


def air():
    air_up, air_down = air_clean[0], air_clean[1]
    pre = 0
    for i in range(1, C-1):
        temp = m[air_up][i]
        m[air_up][i] = pre
        pre = temp
    for i in range(air_up, 0, -1):
        temp, m[i][C-1] = m[i][C-1], pre
        pre = temp
    for i in range(C-1, 0, -1):
        temp, m[0][i] = m[0][i], pre
        pre = temp
    for i in range(air_up):
        temp, m[i][0] = m[i][0], pre
        pre = temp

    pre = 0
    for i in range(1, C-1):
        temp, m[air_down][i] = m[air_down][i], pre
        pre = temp
    for i in range(air_down, R-1):
        temp, m[i][C-1] = m[i][C-1], pre
        pre = temp
    for i in range(C-1, 0, -1):
        temp, m[R-1][i] = m[R-1][i], pre
        pre = temp
    for i in range(R-1, air_down, -1):
        temp, m[i][0] = m[i][0], pre
        pre = temp


answer = 0
while T > 0:
    m = dust()

    air()

    T -= 1

for i in range(R):
    for j in range(C):
        if m[i][j] > 0:
            answer += m[i][j]

print(answer)
