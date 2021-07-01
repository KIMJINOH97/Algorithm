from sys import stdin
from collections import deque

std = stdin.readline
N, M = map(int, std().split())
computer = [[] for i in range(N)]

for i in range(M):
    a, b = map(lambda x: int(x)-1, std().split())
    computer[b].append(a)

q = deque()


def bfs():
    check = [0 for i in range(N)]
    check[q[0]] = 1
    cnt = 0
    while q:
        vertax = q.popleft()
        for v in computer[vertax]:
            if check[v] == 0:
                check[v] = 1
                cnt += 1
                q.append(v)

    return cnt


answer = []
for i in range(N):
    q.append(i)
    answer.append(bfs())

max_ = max(answer)

for i in range(N):
    if answer[i] == max_:
        print(i+1, end=" ")
