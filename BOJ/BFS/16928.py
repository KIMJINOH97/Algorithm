from sys import stdin
from copy import deepcopy
from itertools import combinations

std = stdin.readline

N, M = map(int, std().split())
INF = 99999
board = [-1 for i in range(101)]
sn_la = [-1 for i in range(101)]

for i in range(N+M):
    a, b = map(int, std().split())
    sn_la[a] = b

q = [(1, 0)]
board[1] = 0


def bfs():
    while q:
        v, d = q.pop(0)
        for i in range(1, 7):
            dv = v+i
            if dv <= 100 and board[dv] == -1:
                board[dv] = d+1
                if sn_la[dv] > 0 and board[sn_la[dv]] == -1:
                    board[sn_la[dv]] = d+1
                    q.append((sn_la[dv], d+1))
                elif sn_la[dv] < 0:
                    q.append((dv, d+1))


bfs()
print(board[100])
