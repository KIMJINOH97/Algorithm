from sys import stdin

std = stdin.readline
N, M = map(int, std().split())

dist = [[] for i in range(N)]

for i in range(M):
    v1, v2 = map(int, std().split())
    dist[v1-1].append(v2-1)
    dist[v2-1].append(v1-1)

check = [0 for i in range(N)]
q = []


def dfs():
    while q:
        v = q.pop()
        for ver in dist[v]:
            if check[ver] == 0:
                check[ver] = 1
                q.append(ver)


answer = 0
for i in range(N):
    if check[i] == 0:
        q.append(i)
        dfs()
        answer += 1

print(answer)
