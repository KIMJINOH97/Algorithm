from sys import stdin
from collections import deque

std = stdin.readline

N = int(std())
K = int(std())

board = [[0 for i in range(N)] for j in range(N)]

for i in range(K):
    a, b = map(int, std().split())
    a, b = a-1, b-1
    board[a][b] = 1

R = int(std())
rotate = deque()

for i in range(R):
    time, d = std().split()
    rotate.append((int(time), d))

nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
r, c, dist = 0, 0, 0

board[r][c] = -1
snake = deque()
snake.append((r, c))

t = 0
while True:
    t += 1
    dr, dc = r + nr[dist], c + nc[dist]
    if dr < 0 or dr >= N or dc < 0 or dc >= N or board[dr][dc] == -1:
        break
    r, c = dr, dc
    snake.append((dr, dc))
    if board[dr][dc] != 1:
        tmp_r, tmp_c = snake.popleft()
        board[tmp_r][tmp_c] = 0

    board[dr][dc] = -1

    if len(rotate) > 0 and t == rotate[0][0]:
        if rotate[0][1] == 'D':
            dist = (dist+1) % 4
        else:
            dist = (dist-1) % 4
        rotate.popleft()

print(t)
