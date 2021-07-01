from sys import stdin
from copy import deepcopy
from itertools import combinations

std = stdin.readline

N = int(std())

chess = [[-1 for i in range(N)] for j in range(N)]
q = []

r, c, r1, c1 = map(int, std().split())
chess[r][c] = 0
q.append((r, c, 0))

nr, nc = [-2, -2, 0, 0, 2, 2], [-1, 1, -2, 2, -1, 1]


def bfs():
    while q:
        row, column, d = q.pop(0)
        for i in range(6):
            dr, dc = row+nr[i], column+nc[i]
            if 0 <= dr < N and 0 <= dc < N and chess[dr][dc] == -1:
                chess[dr][dc] = d+1
                q.append((dr, dc, d+1))

    return


bfs()
print(chess[r1][c1])
