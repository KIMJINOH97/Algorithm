from sys import stdin

std = stdin.readline

N = int(std())

dp = [[1000000 for i in range(3)] for j in range(N)]

color = []
for i in range(N):
    color.append(list(map(int, std().split())))


dp[0] = color[0]
# 0 빨강 1 초록 2 파랑
for i in range(1, N):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + color[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + color[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + color[i][2]

print(min(dp[N-1]))
