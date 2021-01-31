from sys import stdin
row, col = map(int, stdin.readline().split())

li = []
for i in range(row):
    li.append(list(map(int, stdin.readline().split())))

for i in range(row):
    for j in range(col):
        if li[i][j] == 2:
            s_r, s_c = i, j

q = []
check = [[0 for i in range(col)] for j in range(row)]

q.append([s_r, s_c])
li[s_r][s_c], check[s_r][s_c] = 0, 1

nr = [0, 1, 0, -1]
nc = [1, 0, -1, 0]

while len(q) != 0:
    r, c = q.pop(0)
    for k in range(4):
        dr, dc = r+nr[k], c+nc[k]
        if 0 <= dr < row and 0 <= dc < col:
            if check[dr][dc] == 0 and li[dr][dc] != 0:
                li[dr][dc] = li[r][c] + 1
                check[dr][dc] = 1
                q.append([dr, dc])

for i in range(row):
    for j in range(col):
        if check[i][j] == 0 and li[i][j] == 1:
            li[i][j] = -1

for i in li:
    for j in i:
        print(j, end=' ')
    print()
