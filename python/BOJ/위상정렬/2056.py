from sys import stdin
from heapq import heappush, heappop

std = stdin.readline

N = int(std())

graph = [[]for i in range(N)]
work = [0 for i in range(N)]
degree = [0 for i in range(N)]

for i in range(N):
    k = list(map(int, std().split()))
    work[i] = k[0]
    for j in range(2, len(k)):
        graph[k[j]-1].append(i)
        degree[i] += 1

q = []
for i in range(N):
    if degree[i] == 0:
        heappush(q, (work[i], i))

answer = 0


def topo_sort():
    global answer
    while q:
        time, vertax = heappop(q)
        answer = time
        for v in graph[vertax]:
            degree[v] -= 1
            if degree[v] == 0:
                heappush(q, (time+work[v], v))


topo_sort()
print(answer)
