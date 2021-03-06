from sys import stdin

std = stdin.readline

N, M = map(int, std().split())

road = []

for i in range(N):
    road.append(list(map(int, std().split())))

check = [[0 for i in range(M)] for j in range(N)]

q = []
nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]


def check_air():
    q.append((0, 0))
    check[0][0] = 1
    while q:
        r, c = q.pop(0)
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < N and 0 <= dc < M and check[dr][dc] == 0 and road[dr][dc] == 0:
                check[dr][dc] = 1
                q.append((dr, dc))


def check_remove_cheese():
    remove_cheese = [[0 for i in range(M)] for j in range(N)]
    cnt = 0
    for i in range(1, N-1):
        for j in range(1, M-1):
            if road[i][j] == 1:
                air_count = 0
                for k in range(4):
                    dr, dc = i+nr[k], j+nc[k]
                    if 0 <= dr < N and 0 <= dc < M and check[dr][dc] == 1:
                        air_count += 1
                if air_count >= 2:
                    remove_cheese[i][j] = 1
                    cnt += 1

    for i in range(N):
        for j in range(M):
            if remove_cheese[i][j] == 1:
                road[i][j] = 0

    return cnt


cheese = 0
for i in range(N):
    for j in range(M):
        if road[i][j] == 1:
            cheese += 1

answer = 0
no_cheese = 0
while no_cheese != cheese:
    check = [[0 for i in range(M)] for j in range(N)]
    check_air()
    no_cheese += check_remove_cheese()
    answer += 1

print(answer)
