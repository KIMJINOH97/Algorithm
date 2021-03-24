from sys import stdin
from heapq import heappop, heappush

std = stdin.readline

N, M = map(int, std().split())
road = [[]for i in range(N)]

for i in range(M):
    a, b, d = map(int, std().split())
    road[a-1].append((b-1, d))
    road[b-1].append((a-1, d))

q = []
INF = 200000000
middle = [[0 for i in range(N)] for j in range(N)]


def dijk(first):
    dist = [[INF, []] for i in range(N)]
    dist[first][0] = 0
    while q:
        d, vertax, path = heappop(q)
        if d > dist[vertax][0]:
            continue
        for ver in road[vertax]:
            v, distance = ver
            if d+distance < dist[v][0]:
                k = path + [v]
                dist[v] = [d+distance, k]
                heappush(q, (dist[v][0], v, k))
    for i in range(N):
        middle[first][i] = '-' if len(dist[i][1]) == 0 else dist[i][1][0]+1


for i in range(N):
    q.append((0, i, []))
    dijk(i)

for i in range(N):
    print(*middle[i])
