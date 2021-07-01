from sys import stdin

std = stdin.readline
R, C = map(int, std().split())

road, water = [], []
end_r, end_c = 0, 0
start_r, start_c = 0, 0
for i in range(R):
    road.append(list(std().rstrip()))

nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
check = [[0 for i in range(C)] for j in range(R)]

for i in range(R):
    for j in range(C):
        if road[i][j] == 'D':
            end_r, end_c = i, j
        elif road[i][j] == '*':
            water.append((i, j, 0))
            check[i][j] = 1
            road[i][j] = 0
        elif road[i][j] == 'S':
            start_r, start_c = i, j


def bfs():
    while water:
        r, c, time = water.pop(0)
        for i in range(4):
            dr, dc = r + nr[i], c + nc[i]
            if 0 <= dr < R and 0 <= dc < C:
                if check[dr][dc] == 0 and not road[dr][dc] in ['D', 'X']:
                    road[dr][dc] = time+1
                    check[dr][dc] = 1
                    water.append((dr, dc, time+1))
    return


def find_S():
    q = []
    check = [[0 for i in range(C)] for j in range(R)]
    q.append((start_r, start_c, 0))
    check[start_r][start_c] = 1
    while q:
        r, c, t = q.pop(0)
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < R and 0 <= dc < C:
                if check[dr][dc] == 0 and not road[dr][dc] in ['X', '*']:
                    if road[dr][dc] == 'D':
                        return t+1
                    if road[dr][dc] == '.' or t+1 < road[dr][dc]:
                        check[dr][dc] = 1
                        q.append((dr, dc, t+1))
    return -1


bfs()
answer = find_S()

print('KAKTUS' if answer == -1 else answer)
