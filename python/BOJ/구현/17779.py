from sys import stdin

std = stdin.readline

N = int(std())

people, region = [], []

for i in range(N):
    people.append(list(map(int, std().split())))


check = [0 for i in range(N)]
xy = []
base = []
answer = 400000


def combi():
    if len(xy) == 2:
        base.append(list(xy))
        return

    for i in range(1, N):
        xy.append(i)
        combi()
        xy.pop()


combi()


def divide(r, c, D1, D2):
    for i in range(D1+1):
        region[r+i][c-i] = 5
        region[r+D2+i][c+D2-i] = 5
    for i in range(D2+1):
        region[r+i][c+i] = 5
        region[r+D1+i][c-D1+i] = 5


def re_divide(r, c, D1, D2):
    how = [0 for i in range(5)]

    for i in range(r+D1):
        for j in range(c+1):
            if region[i][j] == 5:
                break
            region[i][j] = 1
            how[0] += people[i][j]

    for i in range(r+D2+1):
        for j in range(N-1, c, -1):
            if region[i][j] == 5:
                break
            region[i][j] = 2
            how[1] += people[i][j]

    for i in range(r+D1, N):
        for j in range(c-D1+D2):
            if region[i][j] == 5:
                break
            region[i][j] = 3
            how[2] += people[i][j]

    for i in range(r+D2+1, N):
        for j in range(N-1, c-D1+D2-1, -1):
            if region[i][j] == 5:
                break
            region[i][j] = 4
            how[3] += people[i][j]

    for i in range(N):
        for j in range(N):
            if region[i][j] == 5 or region[i][j] == 0:
                how[4] += people[i][j]

    return max(how) - min(how)


for i in range(N):
    for j in range(N):
        x, y = i, j
        for d1, d2 in base:
            if x + d1+d2 < N and y + d2 < N and y-d1 >= 0:
                region = [[0 for _ in range(N)] for __ in range(N)]
                divide(x, y, d1, d2)
                ans = re_divide(x, y, d1, d2)
                if ans < answer:
                    answer = ans

print(answer)
