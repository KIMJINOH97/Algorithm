from sys import stdin
from collections import deque

std = stdin.readline
R, C = 0, 0

building, fire = [], []
q = deque()

nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
answer = 0


def move_person():
    global answer
    new_q = []
    while q:
        r, c, d = q.popleft()
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < R and 0 <= dc < C and building[dr][dc] == '.':
                building[dr][dc] = d+1
                new_q.append((dr, dc, d+1))
            elif dr < 0 or dr >= R or dc < 0 or dc >= C:
                answer = d+1

    return new_q


def move_fire():
    fire_q = []
    for f in fire:
        r, c = f
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < R and 0 <= dc < C and building[dr][dc] != '#' and building[dr][dc] != '*':
                building[dr][dc] = '*'
                fire_q.append((dr, dc))
    return fire_q


T = int(std())
for i in range(T):
    answer = 0
    C, R = map(int, std().split())
    q = deque()
    building, fire = [], []
    for i in range(R):
        building.append(list(std().rstrip()))
        for j in range(C):
            if building[i][j] == '@':
                q.append((i, j, 0))
                building[i][j] = 0
            elif building[i][j] == '*':
                fire.append((i, j))

    while q:
        person = move_person()
        if answer != 0:
            break
        fire = move_fire()
        for p in person:
            p_r, p_c, p_d = p
            if building[p_r][p_c] == '*':
                continue
            q.append(p)
    print(answer if answer != 0 else "IMPOSSIBLE")
