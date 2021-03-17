from sys import stdin
from itertools import combinations
from collections import deque

std = stdin.readline

R, C = map(int, std().split())

arr = []
for i in range(R):
    arr.append(list(map(int, std().split())))
q = deque()
check = [[0 for i in range(C)] for j in range(R)]
nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
region = {0: 0}
region_num = 0
answer = 0


def bfs():
    global answer
    cnt = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < R and 0 <= dc < C and check[dr][dc] == 0 and arr[dr][dc] == 1:
                check[dr][dc] = region_num
                cnt += 1
                q.append((dr, dc))
    region[region_num] = cnt
    return


for i in range(R):
    for j in range(C):
        if arr[i][j] == 1 and check[i][j] == 0:
            region_num += 1
            check[i][j] = region_num
            q.append((i, j))
            bfs()

for i in range(R):
    for j in range(C):
        if arr[i][j] == 0:
            around = []
            for k in range(4):
                dr, dc = i+nr[k], j+nc[k]
                if 0 <= dr < R and 0 <= dc < C:
                    around.append(check[dr][dc])
            around = set(around)
            ans = 1
            for s in around:
                ans += region[s]

            if ans > answer:
                answer = ans

print(answer)
