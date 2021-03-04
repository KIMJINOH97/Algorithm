from sys import stdin
from heapq import heappop, heappush

std = stdin.readline
N = int(std())
M = int(std())

road = [[] for i in range(N)]

for i in range(M):
    a, b, c = map(int, std().split())
    road[a-1].append((b-1, c))

start, end = map(int, std().split())

q = []
INF = 1000000010
heappush(q, (0, start-1))

dist = [INF for i in range(N)]
dist[start-1] = 0


def dijk():
    while q:
        d, vertax = heappop(q)
        if dist[vertax] < d:
            continue
        for v in road[vertax]:
            obj, distance = v
            if d + distance < dist[obj]:
                dist[obj] = d+distance
                heappush(q, (dist[obj], obj))


dijk()
print(dist[end-1])
