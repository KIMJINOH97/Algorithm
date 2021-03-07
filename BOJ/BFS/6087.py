from sys import stdin

std = stdin.readline

column, row = map(int, std().split())

road = []
for i in range(row):
    road.append(list(std().rstrip()))

check = [[-1 for i in range(column)] for j in range(row)]

laser = []

for i in range(row):
    for j in range(column):
        if road[i][j] == 'C':
            laser.append((i, j))


q = [(laser[0][0], laser[0][1], 0)]
check[q[0][0]][q[0][1]] = 0
nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
while q:
    r, c, d = q.pop(0)
    for i in range(4):
        for j in range(1, max(row, column)):
            dr, dc = r + nr[i]*j, c + nc[i]*j
            if 0 <= dr < row and 0 <= dc < column and check[dr][dc] == -1:
                if road[dr][dc] == '*':
                    break
                check[dr][dc] = d + 1
                q.append((dr, dc, d+1))

r, c = laser[1]

print(check[r][c]-1)
