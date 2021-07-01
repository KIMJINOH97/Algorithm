from sys import stdin
from heapq import heappop, heappush

std = stdin.readline

N, M, K = map(int, std().split())

road = [[]for i in range(N)]
road_reverse = [[]for i in range(N)]

for i in range(M):
    a, b, d = map(int, std().split())
    road[a-1].append((b-1, d))
    road_reverse[b-1].append((a-1, d))

inter = list(map(int, std().split()))

INF = 100000000000
q = []
max_d = 0
where = N


def dijk(arr):
    global max_d, where
    dist = [INF for i in range(N)]
    for i in inter:
        dist[i-1] = 0
    while q:
        d, vertax = heappop(q)
        if d > dist[vertax]:
            continue
        for ver in arr[vertax]:
            v, distance = ver
            if d+distance < dist[v]:
                dist[v] = d+distance
                heappush(q, (dist[v], v))

    for i, d in enumerate(dist):
        if d == INF:
            continue
        if max_d <= d:
            if max_d == d and i+1 >= where:
                continue
            max_d = d
            where = i+1


for i in range(K):
    q.append((0, inter[i]-1))

dijk(road_reverse)

print(where)
print(max_d)
