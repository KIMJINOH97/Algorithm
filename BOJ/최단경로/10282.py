from sys import stdin
from heapq import heappop, heappush

std = stdin.readline

T = int(std())
computer, dist = [[]], []

q = []


def dijk():
    while q:
        d, vertax = heappop(q)
        if d > dist[vertax]:
            continue
        for v in computer[vertax]:
            ver, distance = v
            if distance + d < dist[ver]:
                dist[ver] = distance+d
                heappush(q, (distance+d, ver))


INF = 2000000000
while T > 0:
    T -= 1

    N, D, C = map(int, std().split())
    computer = [[] for i in range(N)]
    dist = [INF for i in range(N)]
    dist[C-1] = 0

    for i in range(D):
        a, b, d = map(int, std().split())
        computer[b-1].append((a-1, d))
    q.append((0, C-1))
    dijk()
    m_d, cnt = 0, 0
    for i, d in enumerate(dist):
        if d == INF:
            continue
        cnt += 1
        if d > m_d:
            m_d = d
    print(cnt, m_d)
