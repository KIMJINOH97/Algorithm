from sys import stdin
import copy

row, col = map(int, stdin.readline().split())
cctv = [list(map(int, stdin.readline().split())) for i in range(row)]
cctv_num = []
for i in range(row):
    for j in range(col):
        if 1 <= cctv[i][j] <= 5:
            cctv_num.append((i, j, cctv[i][j]))

answer = 64
nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]  # 오 아래 왼 위


def move(r, c, k):
    while True:
        r = r + nr[k]
        c = c + nc[k]
        if 0 <= r < row and 0 <= c < col and not cctv[r][c] == 6:
            cctv[r][c] = -1
        else:
            break


def dfs(d):
    global cctv, answer
    temp = copy.deepcopy(cctv)
    if d == len(cctv_num):
        zero = 0
        for cc in cctv:
            for c in cc:
                if c == 0:
                    zero += 1
        answer = min(answer, zero)
        return
    r, c, tv = cctv_num[d]
    if tv == 1:
        for i in range(4):
            move(r, c, i)
            dfs(d+1)
            cctv = copy.deepcopy(temp)
    elif tv == 2:
        for i in range(2):  # 0 ,2  1, 3
            move(r, c, i)
            move(r, c, i+2)
            dfs(d+1)
            cctv = copy.deepcopy(temp)
    elif tv == 3:
        for i in range(4):
            move(r, c, i)
            move(r, c, (i+1) % 4)
            dfs(d+1)
            cctv = copy.deepcopy(temp)
    elif tv == 4:
        for i in range(4):
            move(r, c, i)
            move(r, c, (i+1) % 4)
            move(r, c, (i+2) % 4)
            dfs(d+1)
            cctv = copy.deepcopy(temp)
    elif tv == 5:
        for i in range(4):
            move(r, c, i)
        dfs(d+1)
        cctv = copy.deepcopy(temp)
    return


dfs(0)
print(answer)
