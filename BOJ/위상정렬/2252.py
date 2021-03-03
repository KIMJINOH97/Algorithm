from sys import stdin

std = stdin.readline

N, M = map(int, std().split())

check = [0 for i in range(N)]
edge = [[] for i in range(N)]

degree = [0 for i in range(N)]

for i in range(M):
    a, b = map(int, std().split())
    edge[a-1].append(b-1)
    degree[b-1] += 1

q = []

for i in range(N):
    if degree[i] == 0:
        q.append(i)

answer = []
while q:
    vertax = q.pop(0)
    answer.append(vertax)

    for v in edge[vertax]:
        degree[v] -= 1
        if degree[v] == 0:
            q.append(v)

for a in answer:
    print(a+1, end=" ")
