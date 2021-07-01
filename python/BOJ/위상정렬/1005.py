from sys import stdin
from heapq import heapify, heappop, heappush

std = stdin.readline

T = int(std())


def topo():
    while q:
        t, vertax = heappop(q)

        for v in edge[vertax]:
            degree[v] -= 1
            if degree[v] == 0:
                dp[v] = t+time[v]
                heappush(q, (t+time[v], v))


answer = []
while T > 0:
    T -= 1
    N, K = map(int, std().split())
    edge = [[] for i in range(N)]
    degree = [0 for i in range(N)]
    dp = [0 for i in range(N)]
    time = list(map(int, std().split()))

    for i in range(K):
        a, b = map(int, std().split())
        edge[a-1].append(b-1)
        degree[b-1] += 1
    W = int(std())
    q = []
    for i in range(N):
        if degree[i] == 0:
            dp[i] = time[i]
            heappush(q, (time[i], i))

    topo()
    answer.append(dp[W-1])

for a in answer:
    print(a)
