from sys import stdin


std = stdin.readline

N, M = map(int, std().split())

arr = [[0 for i in range(N+1)]]

for i in range(N):
    arr.append([0]+list(map(int, std().split())))

D = [[0 for i in range(N+1)] for j in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        D[i][j] = D[i-1][j] + D[i][j-1] - D[i-1][j-1] + arr[i][j]

answer = []
for i in range(M):
    r, c, r1, c1 = map(lambda x: int(x), std().split())
    answer.append(D[r1][c1]-D[r-1][c1]-D[r1][c-1]+D[r-1][c-1])

for a in answer:
    print(a)
