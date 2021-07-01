from sys import stdin
row, col = map(int, stdin.readline().split())

ice = [list(map(int, stdin.readline().split())) for i in range(row)]

nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]


def melt():
    after = []
    for i in range(row):
        for j in range(col):
            count = 0
            if ice[i][j] != 0:
                for k in range(4):
                    dr, dc = i+nr[k], j+nc[k]
                    if 0 <= dr < row and 0 <= dc < col:
                        if ice[dr][dc] == 0:
                            count += 1
            if count != 0:
                after.append((i, j, count))

    for a in after:
        i, j, c = a
        ice[i][j] = ice[i][j]-c if ice[i][j]-c >= 0 else 0


q = []
check = [[0 for i in range(col)] for j in range(row)]


def bfs():
    while q:
        r, c = q.pop(0)
        for k in range(4):
            dr, dc = r+nr[k], c+nc[k]
            if 0 <= dr < row and 0 <= dc < col:
                if not check[dr][dc] and ice[dr][dc] != 0:
                    #print(dr, dc)
                    check[dr][dc] = 1
                    q.append((dr, dc))

    return


s, all = 0, False
while True:
    count = 0
    for i in range(row):
        for j in range(col):
            if ice[i][j] != 0 and check[i][j] == 0:
                count += 1
                check[i][j] = 1
                q.append((i, j))
                bfs()
    melt()
    if count == 0:
        all = True
        break
    if count >= 2:
        break
    check = [[0 for i in range(col)] for j in range(row)]
    s += 1

if all:
    print("0")
else:
    print(s)
