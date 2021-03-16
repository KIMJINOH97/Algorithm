from sys import stdin
from copy import deepcopy

std = stdin.readline
R, C = map(int, std().split())

Map, land = [], []
for i in range(R):
    Map.append(list(std().rstrip()))
    for j in range(C):
        if Map[i][j] == 'L':
            land.append((i, j))

q = []
nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs():
    check = [[0 for j in range(C)]for i in range(R)]
    check[q[0][0]][q[0][1]] = 1
    dist = 0
    while q:
        r, c, d = q.pop(0)
        if d > dist:
            dist = d
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < R and 0 <= dc < C and check[dr][dc] == 0 and Map[dr][dc] == 'L':
                check[dr][dc] = 1
                q.append((dr, dc, d+1))

    return dist


answer = 0
while land:
    r, c = land.pop(0)
    q.append((r, c, 0))
    ans = bfs()
    if ans > answer:
        answer = ans

print(answer)
