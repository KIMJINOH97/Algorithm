from sys import stdin
from heapq import heappush, heappop

std = stdin.readline

N, M = map(int, std().split())

friend = [[]for i in range(N)]

for i in range(M):
    a, b = map(int, std().split())
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)

q = []


def bfs(k):
    dist = [-1 for i in range(N)]
    q.append((k, 0))
    dist[k] = 0
    while q:
        vertax, d = q.pop(0)
        for v in friend[vertax]:
            if dist[v] == -1:
                dist[v] = d+1
                q.append((v, d+1))

    return sum(dist)


answer = []

for i in range(N):
    answer.append((bfs(i), i))

answer = sorted(answer, key=lambda x: (x[0], x[1]))

print(answer[0][1]+1)
