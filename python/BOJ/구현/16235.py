from sys import stdin
from collections import deque
from copy import deepcopy

std = stdin.readline

N, M, K = map(int, std().split())

A = []
food = [[5 for j in range(N)] for i in range(N)]
for i in range(N):
    A.append(list(map(int, std().split())))


life = [[[] for j in range(N)] for i in range(N)]

for i in range(M):
    r, c, year = map(int, std().split())
    r, c = r-1, c-1
    life[r][c].append(year)

global dead
dead = []


def spring():
    for i in range(N):
        for j in range(N):
            if len(life[i][j]) == 0:
                continue
            if len(life[i][j]) == 1:
                if life[i][j][0] <= food[i][j]:
                    food[i][j] -= life[i][j][0]
                    life[i][j][0] += 1
                else:
                    dead.append((i, j, life[i][j].pop()))
            else:
                newbie = []
                for l in sorted(life[i][j]):
                    if l <= food[i][j]:
                        food[i][j] -= l
                        newbie.append(l+1)
                    else:
                        dead.append((i, j, l))
                life[i][j] = newbie

    return


def summer():
    global dead
    for r, c, d in dead:
        food[r][c] += d // 2
    dead = []
    return


nr, nc = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]


def fall():
    dic = {}
    for i in range(N):
        for j in range(N):
            for tree in life[i][j]:
                if tree % 5 == 0:
                    if (i, j) in dic:
                        dic[(i, j)] += 1
                    else:
                        dic[(i, j)] = 1

    for key in dic:
        r, c = key
        for j in range(8):
            dr, dc = r + nr[j], c + nc[j]
            if dr < 0 or dc < 0 or dr >= N or dc >= N:
                continue
            for k in range(dic[key]):
                life[dr][dc].append(1)

    return


def winter():
    for i in range(N):
        for j in range(N):
            food[i][j] += A[i][j]
    return


for i in range(K):
    spring()
    summer()
    fall()
    winter()

answer = 0
for i in range(N):
    for j in range(N):
        answer += len(life[i][j])

print(answer)
