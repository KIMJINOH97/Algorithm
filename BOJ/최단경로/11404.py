from sys import stdin

std = stdin.readline

N = int(std())

M = int(std())
INF = 1000000001
edge = [[INF for i in range(N)]for i in range(N)]
for i in range(M):
    a, b, d = map(int, std().split())
    if d < edge[a-1][b-1]:
        edge[a-1][b-1] = d
for i in range(N):
    for j in range(N):
        if i == j:
            edge[i][j] = 0


for k in range(N):
    for i in range(N):
        for j in range(N):
            if edge[i][k] + edge[k][j] < edge[i][j]:
                edge[i][j] = edge[i][k] + edge[k][j]

for i in range(N):
    for j in range(N):
        if edge[i][j] >= INF:
            print("0", end=" ")
        else:
            print(edge[i][j], end=" ")
    print()
