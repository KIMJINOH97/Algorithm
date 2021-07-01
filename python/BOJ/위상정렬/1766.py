from sys import stdin
from heapq import heapify, heappop, heappush

std = stdin.readline

N, M = map(int, std().split())

book = [[] for i in range(N)]
degree = [0 for i in range(N)]

for i in range(M):
    a, b = map(int, std().split())
    book[a-1].append(b-1)
    degree[b-1] += 1
q, answer = [], []

for i in range(N):
    if degree[i] == 0:
        heappush(q, i)

while q:
    vertax = heappop(q)
    answer.append(vertax)
    for v in book[vertax]:
        degree[v] -= 1
        if degree[v] == 0:
            heappush(q, v)

for a in answer:
    print(a+1, end=" ")
