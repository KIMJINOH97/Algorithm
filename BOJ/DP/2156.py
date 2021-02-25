from sys import stdin

std = stdin.readline

N = int(std())

grape = []
for i in range(N):
    grape.append(int(std()))

dp = [[0 for j in range(3)] for i in range(N)]

dp[0][1] = grape[0]
if N >= 2:
    dp[1][1] = grape[1]
for i in range(1, N):
    dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
    if i >= 2:
        dp[i][1] = dp[i-1][0] + grape[i]
    dp[i][2] = dp[i-1][1] + grape[i]

print(max(map(max, dp)))
