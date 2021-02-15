from sys import stdin
from copy import deepcopy

std = stdin.readline
lab = []
N, T = map(int, std().split())
for i in range(N):
    lab.append(list(map(int, std().split())))

virus = []
for i in range(N):
    for j in range(N):
        if lab[i][j] == 1:
            lab[i][j] = -1
        elif lab[i][j] == 2:
            lab[i][j] = -3
            virus.append((i, j))
virus_combi, c = [], []
check = [0 for i in range(len(virus))]


def combi(n, start):
    if len(c) == n:
        virus_combi.append(list(c))
        return

    for i in range(start, len(virus)):
        if check[i] == 0:
            check[i] = 1
            c.append(virus[i])
            combi(n, i+1)
            c.pop()
            check[i] = 0


combi(T, 0)
a, q = [], []
nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]


def bfs():
    while q:
        r, c, d = q.pop(0)
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < N and 0 <= dc < N and (a[dr][dc] == 0 or a[dr][dc] == -3):
                a[dr][dc] = d+1
                q.append((dr, dc, d+1))


answer = 2501


for vi in virus_combi:
    a, ans = deepcopy(lab), 0
    for v in vi:
        r, c = v
        a[r][c] = -2  # 활성상태는 -2로하자
        q.append((r, c, 0))

    bfs()
    for i in range(N):
        flag = False
        for j in range(N):
            if a[i][j] == 0:
                ans = -1
                flag = True
                break
            elif a[i][j] > 0 and not lab[i][j] == -3:
                if a[i][j] > ans:
                    ans = a[i][j]
        if flag:
            break
    if ans >= 0 and answer > ans:
        answer = ans


print("-1" if answer == 2501 else answer)
