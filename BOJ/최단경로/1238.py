from sys import stdin
from heapq import heappush, heappop

std = stdin.readline

N, M, x = map(int, std().split())

INF = 1000000001
# 순방향 간선
road = [[]for i in range(N)]

# 역방향 간선  //  다른 지점으로 부터 올 수 있는 거리를 구하기 위함
road_reverse = [[]for i in range(N)]

for i in range(M):
    a, b, d = map(int, std().split())
    road[a-1].append((b-1, d))
    road_reverse[b-1].append((a-1, d))

x = x-1
q = [(0, x)]


def dijkstra(k, func):
    dist = [INF for i in range(N)]
    dist[k] = 0

    while q:
        distance, vertax = heappop(q)
        if distance > dist[vertax]:
            continue
        for v in func[vertax]:
            ver, d = v
            if distance + d < dist[ver]:
                dist[ver] = distance + d
                heappush(q, (dist[ver], ver))

    return dist


go = dijkstra(x, road)
q.append((0, x))
back = dijkstra(x, road_reverse)
answer = 0

for i in range(N):
    if go[i] == INF or back[i] == INF or i == x:
        continue
    if answer < go[i]+back[i]:
        answer = go[i]+back[i]

print(answer)
