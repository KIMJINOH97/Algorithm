from sys import stdin

std = stdin.readline

N, M = map(int, std().split())

parent = [0 for i in range(N+1)]

for i in range(N+1):
    parent[i] = i


def find(a):
    if parent[a] == a:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    parent_a = find(a)
    parent_b = find(b)

    if parent_b < parent_a:
        parent[parent_a] = parent_b
    else:
        parent[parent_b] = parent_a


truth = list(map(int, std().split()))

#  진실을 말한 자
for i in range(1, 1 + truth[0]):
    parent[truth[i]] = 0

party_list = []

for i in range(M):
    party = list(map(int, std().split()))
    party = party[1:]
    flag = False
    for j in range(len(party)-1):
        union(party[j], party[j+1])

    party_list.append(party)

answer = 0
for party in party_list:
    flag = False
    for p in party:
        if find(p) == 0:
            flag = True
            break

    if not flag:
        answer += 1

print(answer)
