from sys import stdin

std = stdin.readline

N, M, K = map(int, std().split())

parent = [0 for i in range(N+1)]

for i in range(N+1):
    parent[i] = i

money = list(map(int, std().split()))


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_a < parent_b:
        parent[parent_b] = parent_a
    else:
        parent[parent_a] = parent_b


for i in range(M):
    a, b = map(int, std().split())
    union(a, b)

money_sort = []
for i in range(N):
    money_sort.append((money[i], i+1))

money_sort = sorted(money_sort, key=lambda x: x[0])

answer = 0
for m in money_sort:
    cost, f = m
    root_f = find(f)
    if root_f != 0:
        parent[root_f] = 0
        answer += cost

print(answer if answer <= K else "Oh no")
