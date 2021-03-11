from sys import stdin
from copy import deepcopy
from itertools import permutations

std = stdin.readline

N = int(std())
friend = [[]for i in range(N)]

M = int(std())
for i in range(M):
    a, b = map(int, std().split())
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)

dist = [-1 for i in range(N)]

q = [(0, 0)]
dist[0] = 0
cnt = 0
while q:
    f, d = q.pop(0)
    if d == 3:
        break
    elif 0 < d <= 2:
        cnt += 1
    for fr in friend[f]:
        if dist[fr] == -1:
            dist[fr] = d+1
            q.append((fr, d+1))

print(cnt)
