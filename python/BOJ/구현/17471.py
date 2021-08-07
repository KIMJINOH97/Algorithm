from sys import stdin
from itertools import combinations

std = stdin.readline
N = int(std())

city = [i for i in range(N)]
edge = [[] for i in range(N)]
people = list(map(int, std().split()))

allOfPeople = sum(people)
q = []

for i in range(N):
    li = list(map(int, std().split()))
    cnt = li[0]
    li = list(map(lambda x: x-1, li[1:]))
    for j in range(cnt):
        edge[i].append(li[j])
        edge[li[j]].append(i)

for i in range(len(edge)):
    edge[i] = list(set(edge[i]))


def bfs(dic):
    while q:
        vertax = q.pop(0)
        for ver in edge[vertax]:
            if ver not in dic:
                continue

            if dic[ver] == 1:
                continue
            else:
                dic[ver] = 1
                q.append(ver)
    for key in dic:
        if dic[key] == 0:
            return False

    return True


def checkIsConnect(A):
    dicA = {key: 0 for key in A}
    dicB = {}
    q.append(A[0])
    dicA[A[0]] = 1
    if not bfs(dicA):
        return False

    for i in range(N):
        if i not in dicA:
            dicB[i] = 0
            if len(q) == 0:
                q.append(i)
                dicB[i] = 1

    return bfs(dicB)


def sumOf(A):
    cnt = 0
    for a in A:
        cnt += people[a]
    return cnt


INF = 10000000
answer = INF
for i in range(1, N//2 + 1):
    for A in combinations(city, i):
        q = []
        result = checkIsConnect(A)
        if result:
            APeople = sumOf(A)
            answer = min(answer, abs(APeople - (allOfPeople - APeople)))

print(answer if answer != INF else -1)
