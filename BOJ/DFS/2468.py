from sys import stdin
from copy import deepcopy

std = stdin.readline

N = int(std())

reg, region = [], []
for i in range(N):
    reg.append(list(map(int, std().split())))


nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]


s, check = [], [[0 for i in range(N)] for j in range(N)]


def dfs():
    while s:
        r, c = s.pop()
        for i in range(4):
            dr = r + nr[i]
            dc = c + nc[i]
            if 0 <= dr < N and 0 <= dc < N and region[dr][dc] >= 0 and check[dr][dc] == 0:
                check[dr][dc] = 1
                s.append((dr, dc))


def safezone(height):
    for i in range(N):
        for j in range(N):
            if region[i][j] <= height:
                region[i][j] = -1
    answer = 0
    for i in range(N):
        for j in range(N):
            if check[i][j] == 0 and region[i][j] > height:
                s.append((i, j))
                check[i][j] = 1
                dfs()
                answer += 1
    return answer


ans = 0

max_height = max(map(max, reg))

for i in range(0, max_height):
    check = [[0 for i in range(N)] for j in range(N)]
    region = deepcopy(reg)
    zone = safezone(i)
    ans = max(zone, ans)


print(ans)
