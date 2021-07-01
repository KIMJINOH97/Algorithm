from sys import stdin

N, M = map(int, stdin.readline().split())
city = [list(map(int, stdin.readline().split())) for i in range(N)]
home, chicken = [], []
for i in range(N):
    for j in range(N):
        if city[i][j] == 1:
            home.append((i, j))
        if city[i][j] == 2:
            chicken.append((i, j))
combi_chicken = []
check = [0 for i in range(len(chicken))]
what = []


def combi(n, start):
    if len(what) == n:
        combi_chicken.append(list(what))
        return
    for i in range(start, len(chicken)):
        if check[i] == 0:
            check[i] = 1
            what.append(chicken[i])
            combi(n, i+1)
            check[i] = 0
            what.pop()


combi(M, 0)
answer = 999999999
for chick in combi_chicken:
    dis = 0
    for h in home:
        min_chick_dis = 999999999
        for c in chick:
            d = abs(c[0] - h[0]) + abs(c[1] - h[1])
            if d < min_chick_dis:
                min_chick_dis = d
        dis += min_chick_dis
    if dis < answer:
        answer = dis

print(answer)
