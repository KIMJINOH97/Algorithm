from sys import stdin
from heapq import heappop, heappush

std = stdin.readline

n = int(std())
m = int(std())

INF = 1999999999
road = [[] for i in range(n)]

for i in range(m):
    a, b, d = map(lambda x: int(x), std().split())
    road[a-1].append((b-1, d))

start, end = map(lambda x: int(x)-1, std().split())

dist = [INF for i in range(n)]
dist[start] = 0

q = [(0, start)]
end_path = [[] for i in range(n)]


def dijk():
    while q:
        distance, vertax = heappop(q)
        if distance > dist[vertax]:
            continue

        for v in road[vertax]:
            ver, d = v
            if distance + d < dist[ver]:
                if ver == end:
                    end_path
                dist[ver] = distance+d
                end_path[ver] = end_path[vertax]+[vertax]
                heappush(q, (dist[ver], ver))

    return


dijk()
print(dist[end])
end_path[end].append(end)
print(len(end_path[end]))
for e in end_path[end]:
    print(e+1, end=" ")
