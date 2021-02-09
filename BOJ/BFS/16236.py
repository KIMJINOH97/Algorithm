from sys import stdin

std = stdin.readline
N = int(std())
shark = []

for i in range(N):
    shark.append(list(map(int, std().split())))

huge, baby, eat = 2, [0, 0], 0  # 아기상어 크기, 위치, 현재먹은 개수
for i in range(N):
    for j in range(N):
        if shark[i][j] == 9:
            baby = [i, j]

q = []
nr, nc = [-1, 0, 1, 0], [0, -1, 0, 1]

check = [[0 for i in range(N)] for j in range(N)]


def find_food():
    check = [[0 for i in range(N)] for j in range(N)]
    f_r, f_c, dd = q[-1]
    check[f_r][f_c] = 1
    F = []
    dist = -1
    while q:
        r, c, d = q.pop(0)
        if d == dist:
            break
        for i in range(4):
            dr = r + nr[i]
            dc = c + nc[i]
            if 0 <= dr < N and 0 <= dc < N:
                if check[dr][dc] == 0 and shark[dr][dc] <= huge:
                    check[dr][dc] = 1
                    if 0 < shark[dr][dc] < huge:
                        F.append((dr, dc, d+1))
                        dist = d+1
                    q.append((dr, dc, d+1))
    F = sorted(F, key=lambda x: (x[2], x[0], x[1]))
    if len(F) == 0:
        return -1
    else:
        return F[0]


answer = 0
aa = 0
food = []
while True:
    r, c = baby
    q.append((r, c, 0))
    food = find_food()
    if food == -1:
        break
    q = []
    shark[r][c] = 0
    new_r, new_c, dist = food
    baby = [new_r, new_c]
    shark[new_r][new_c] = 9
    eat += 1
    answer += dist

    if huge == eat:
        huge += 1
        eat = 0

print(answer)
