from sys import stdin
from copy import deepcopy

std = stdin.readline

N, M = map(int, std().split())

nr, nc = [0, -1, -1, -1, 0, 1, 1, 1], [-1, -1, 0, 1, 1, 1, 0, -1]

basket = []
groom = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]

for i in range(N):
    basket.append(list(map(int, std().split())))


def rain():
    for g in groom:
        r, c = g
        basket[r][c] += 1

    return None


def moveGroom(d, s):
    move = []
    for r, c in groom:
        dr, dc = r + nr[d] * s, c + nc[d] * s
        move.append((dr % N, dc % N))

    return move


def copyWaterBug():
    newBasket = deepcopy(basket)
    for r, c in groom:
        cnt = 0
        for i in range(1, 8, 2):
            dr, dc = r + nr[i], c + nc[i]
            if dr < 0 or dr >= N or dc < 0 or dc >= N or basket[dr][dc] == 0:
                continue
            cnt += 1
        newBasket[r][c] += cnt

    return newBasket


def makeGroom():
    newGroom = []
    dic = {}
    for g in groom:
        dic[g] = 1

    for i in range(N):
        for j in range(N):
            if basket[i][j] >= 2 and (i, j) not in dic:
                basket[i][j] -= 2
                newGroom.append((i, j))

    return newGroom


for i in range(M):
    d, s = map(int, std().split())  # d 이동방향, s 횟수
    groom = moveGroom(d - 1, s)
    rain()
    basket = copyWaterBug()
    groom = makeGroom()

print(sum(map(sum, basket)))
