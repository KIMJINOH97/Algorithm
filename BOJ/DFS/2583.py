from sys import stdin

std = stdin.readline

M, N, K = map(int, std().split())

square = []
for i in range(K):
    square.append(list(map(int, std().split())))

board = [[0 for i in range(N)] for j in range(M)]

for b in square:
    col1, row1, col2, row2 = b
    for i in range(row1, row2):
        for j in range(col1, col2):
            board[i][j] = 1

nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]

s = []


def dfs():
    size = 1
    while s:
        r, c = s.pop()
        for i in range(4):
            dr = r + nr[i]
            dc = c + nc[i]
            if 0 <= dr < M and 0 <= dc < N and board[dr][dc] == 0:
                board[dr][dc] = 1
                s.append((dr, dc))
                size += 1
    return size


si = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            s.append((i, j))
            board[i][j] = 1
            size = dfs()
            si.append(size)

si.sort()
print(len(si))
print(*si)
