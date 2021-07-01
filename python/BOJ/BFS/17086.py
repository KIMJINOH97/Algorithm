from sys import stdin

std = stdin.readline

R, C = map(int, std().split())

arr = []
for i in range(R):
    arr.append(list(map(int, std().split())))

nr, nc = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

q = []
check = [[-1 for i in range(C)] for j in range(R)]

for i in range(R):
    for j in range(C):
        if arr[i][j] == 1:
            q.append((i, j, 0))
            check[i][j] = 0

while q:
    r, c, d = q.pop(0)

    for i in range(8):
        dr, dc = r+nr[i], c+nc[i]
        if 0 <= dr < R and 0 <= dc < C and check[dr][dc] == -1:
            check[dr][dc] = d+1
            q.append((dr, dc, d+1))


print(max(map(max, check)))
