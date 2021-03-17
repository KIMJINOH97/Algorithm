from sys import stdin
from itertools import combinations
from collections import deque

std = stdin.readline

N, M = map(int, std().split())

singer = [[]for i in range(N+1)]
degree = [0 for i in range(N+1)]

for i in range(M):
    order = list(map(int, std().split()))
    K = order[0]
    order = order[1:]
    n = 0
    while n != K-1:
        for j in range(n+1, K):
            singer[order[n]].append(order[j])
            degree[order[j]] += 1
        n += 1

q = deque()

for i in range(1, N+1):
    if degree[i] == 0:
        q.append(i)

answer = []


def topolo_sort():
    while q:
        vertax = q.popleft()
        answer.append(vertax)
        for v in singer[vertax]:
            degree[v] -= 1
            if degree[v] == 0:
                q.append(v)


topolo_sort()
if len(answer) != N:
    print("0")
else:
    for a in answer:
        print(a)
