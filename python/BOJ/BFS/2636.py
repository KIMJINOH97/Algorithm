from sys import stdin
from copy import deepcopy

std = stdin.readline
N, M = map(int, std().split())
cheese = []
for i in range(N):
    cheese.append(list(map(int, std().split())))

nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
check = deepcopy(cheese)
answer, time = 0, 0
q = []


def air():
    q.append((0, 0))
    ch = [[0 for i in range(M)] for j in range(N)]
    while q:
        r, c = q.pop(0)
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < N and 0 <= dc < M:
                if ch[dr][dc] == 0 and not cheese[dr][dc] == 1:
                    ch[dr][dc] = 1
                    cheese[dr][dc] = -1
                    q.append((dr, dc))


while True:
    if max(map(max, cheese)) == 0:
        break
    count = 0
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == 1:
                count += 1
    answer = count
    air()
    for i in range(N):
        for j in range(M):
            if cheese[i][j] == -1:
                for k in range(4):
                    r = i+nr[k]
                    c = j+nc[k]
                    if 0 <= r < N and 0 <= c < M:
                        check[r][c] = 0

    cheese = deepcopy(check)
    time += 1

print(time)
print(answer)
