from sys import stdin
from heapq import heappush, heappop

std = stdin.readline

V, E = map(int, std().split())

INF = 1000000001
edge = [[]for i in range(V)]

for i in range(E):
    a, b, d = map(int, std().split())
    edge[a-1].append((b-1, d))
    edge[b-1].append((a-1, d))

q = []


def prim():
    dist = [INF for i in range(V)]
    check = [0 for i in range(V)]
    dist[0] = 0
    check[0] = True
    for v in edge[0]:
        ver, d = v
        dist[ver] = d
        heappush(q, (d, ver))

    while q:
        distance, vertax = heappop(q)
        check[vertax] = True
        for v in edge[vertax]:
            ver, d = v
            if not check[ver] and d < dist[ver]:
                dist[ver] = d
                heappush(q, (d, ver))

    cnt = 0
    for d in dist:
        cnt += d

    return cnt


print(prim())
