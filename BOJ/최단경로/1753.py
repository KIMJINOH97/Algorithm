from sys import stdin
import heapq

INF = 99999999

N, V = map(int, stdin.readline().split())
start_num = int(stdin.readline())-1
li = [[] for i in range(N)]
dist = [INF for i in range(N)]

for i in range(V):
    a, b, c = map(int, stdin.readline().split())
    li[a-1].append((b-1, c))

hq = []
dist[start_num] = 0


def dijk():
    heapq.heappush(hq, (0, start_num))
    while len(hq) != 0:
        dis, ver = heapq.heappop(hq)
        if dist[ver] < dis:
            continue
        for i in range(len(li[ver])):
            if dist[li[ver][i][0]] > dis + li[ver][i][1]:
                dist[li[ver][i][0]] = dis + li[ver][i][1]
                heapq.heappush(hq, (dist[li[ver][i][0]], li[ver][i][0]))
    return


dijk()

for i in range(N):
    if dist[i] != INF:
        print(dist[i])
    else:
        print("INF")
