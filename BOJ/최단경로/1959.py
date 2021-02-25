from sys import stdin
from heapq import heappop, heappush

std = stdin.readline

INF = 4000000
V, E = map(int, std().split())
road = [[]for i in range(V)]
for i in range(E):
    a, b, d = map(int, std().split())
    road[a-1].append((b-1, d))

q = []


def dijk(k):
    dist = [INF for i in range(V)]
    while q:
        b, d = heappop(q)
        if dist[b] < d:
            continue
        for dis in road[b]:
            next_vertax, distance = dis
            if d + distance < dist[next_vertax]:
                dist[next_vertax] = d+distance
                heappush(q, (next_vertax, d+distance))
    return dist[k]


answer = INF
for i in range(V):
    heappush(q, (i, 0))
    path = dijk(i)
    if path < answer:
        answer = path

print(answer if answer != INF else "-1")
