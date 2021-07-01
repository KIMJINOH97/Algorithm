from sys import stdin
from copy import deepcopy

std = stdin.readline

chess = []
N = 8

wall = []
for i in range(N):
    chess.append(list(std().rstrip()))
    for j in range(N):
        if chess[i][j] == '#':
            wall.append([i, j])

nr, nc = [0, 0, 1, 1, 1, 0, -1, -1, -1], [0, 1, 1, 0, -1, -1, -1, 0, 1]

q = [(N-1, 0)]


def bfs_1():
    new_q = []
    while q:
        r, c = q.pop(0)
        for i in range(9):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < N and 0 <= dc < N and chess[dr][dc] != '#':
                new_q.append((dr, dc))
    new_q = list(set(new_q))
    return new_q


def move_wall():
    global wall
    new_wall = []
    for i in range(len(wall)):
        r, c = wall[i][0], wall[i][1]
        chess[r][c] = '.'
        if r+1 >= N:
            continue
        wall[i][0] += 1
        new_wall.append(wall[i])

    wall = deepcopy(new_wall)

    for w in wall:
        r, c = w
        chess[r][c] = '#'


answer = 0

while q:
    m = bfs_1()
    move_wall()
    for i in range(len(m)):
        r, c = m[i]
        if chess[r][c] == '#':
            continue
        q.append((r, c))
        if r == 0 and c == 7:
            answer = 1
    if answer:
        break

print(answer)
