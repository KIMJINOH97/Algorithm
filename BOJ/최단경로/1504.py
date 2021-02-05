from sys import stdin
from heapq import heappop, heappush

INF = 800001
std = stdin.readline
N, E = map(int, std().split())
ver = [[] for i in range(N)]

for i in range(E):
    a, b, c = map(int, std().split())
    ver[a-1].append((b-1, c))
    ver[b-1].append((a-1, c))

ver1, ver2 = map(int, std().split())
ver1, ver2 = ver1-1, ver2-1
hq = []


def dijk(dijkstra):
    while hq:
        v1, dis = heappop(hq)
        if dijkstra[v1] < dis:
            continue
        for vertax in ver[v1]:
            v, d = vertax
            if dijkstra[v] > dis+d:
                dijkstra[v] = dis+d
                heappush(hq, (v, dijkstra[v]))


di = [INF for i in range(N)]  # 1번에서 다익
heappush(hq, (0, 0))
di[0] = 0
dijk(di)

one_to_ver1 = di[ver1]  # 1->ver1
one_to_ver2 = di[ver2]  # 1->ver2

ver1_dijk = [INF for i in range(N)]
ver2_dijk = [INF for i in range(N)]

heappush(hq, (ver1, 0))
ver1_dijk[ver1] = 0
dijk(ver1_dijk)


heappush(hq, (ver2, 0))
ver2_dijk[ver2] = 0
dijk(ver2_dijk)

one_to_ver1 += ver1_dijk[ver2]+ver2_dijk[N-1]  # 1->ver1->ver2
one_to_ver2 += ver2_dijk[ver1]+ver1_dijk[N-1]  # 1->ver2->ver1

answer = min(one_to_ver1, one_to_ver2)

if answer >= INF:
    print("-1")
else:
    print(answer)
