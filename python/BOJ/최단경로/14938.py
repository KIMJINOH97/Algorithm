from sys import stdin
from heapq import heappop, heappush

std = stdin.readline

n, m, r = map(int, std().split())

INF = 1000000001
item = list(map(int, std().split()))
edge = [[]for i in range(n)]

for i in range(r):
    a, b, d = map(int, std().split())
    a, b = a-1, b-1
    edge[a].append((b, d))
    edge[b].append((a, d))

q = []


def dijkstra(k):
    dist = [INF for i in range(n)]
    dist[k] = 0
    while q:
        distance, vertax = heappop(q)
        if distance > dist[vertax]:
            continue

        for v in edge[vertax]:
            ver, d = v
            if distance + d < dist[ver]:
                dist[ver] = distance + d
                heappush(q, (dist[ver], ver))

    cnt = 0
    for i, d in enumerate(dist):
        if d <= m:
            cnt += item[i]
    return cnt


answer = 0

for i in range(n):
    heappush(q, (0, i))
    ans = dijkstra(i)
    if ans > answer:
        answer = ans

print(answer)
