from sys import stdin

std = stdin.readline

N = int(std())

arr = []

for i in range(N):
    arr.append(list(map(int, std().split())))

nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]

end_point = []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            for k in range(4):
                dr, dc = i + nr[k], j+nc[k]
                if 0 <= dr < N and 0 <= dc < N:
                    if arr[dr][dc] == 0:
                        end_point.append((i, j, 0))
                        break

q, region = [], []


def bfs(e):
    a, b, dist = e
    check = [[-1 for i in range(N)] for j in range(N)]
    check[a][b] = 0
    while region:
        r, c, d = region.pop(0)
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < N and 0 <= dc < N and arr[dr][dc] == 1 and check[dr][dc] == -1:
                check[dr][dc] = 0
                region.append((dr, dc, 0))

    while q:
        r, c, d = q.pop(0)
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < N and 0 <= dc < N and arr[dr][dc] != 1 and check[dr][dc] == -1:
                check[dr][dc] = d+1
                q.append((dr, dc, d+1))

    cnt = 10000000
    for i in range(N):
        for j in range(N):
            if check[i][j] in [-1, 0]:
                continue
            for k in range(4):
                dr, dc = i+nr[k], j+nc[k]
                if 0 <= dr < N and 0 <= dc < N and check[dr][dc] == -1:
                    if check[i][j] < cnt:
                        cnt = check[i][j]

    # for i in range(N):
     #   print(check[i])
    return cnt


answer = 10000000
for e in end_point:
    q.append(e)
    region.append(e)
    result = bfs(e)
    if result < answer:
        answer = result

print(answer)
