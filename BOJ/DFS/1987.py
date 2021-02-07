from sys import stdin

std = stdin.readline

R, C = map(int, std().split())
board = [list(std().rstrip()) for j in range(R)]
alpha = [0 for i in range(26)]

s = []
nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]

answer = 1


def dfs(depth, row, col):
    global answer
    if depth > answer:
        answer = depth
    if answer == R*C:
        return
    for i in range(4):
        dr = row + nr[i]
        dc = col + nc[i]
        if 0 <= dr < R and 0 <= dc < C and alpha[ord(board[dr][dc])-65] == 0:
            k = ord(board[dr][dc])-65
            alpha[k] = 1
            dfs(depth+1, dr, dc)
            alpha[k] = 0


alpha[ord(board[0][0])-65] = 1
dfs(1, 0, 0)
print(answer)
