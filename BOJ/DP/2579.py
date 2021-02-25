from sys import stdin

std = stdin.readline

N = int(std())

step = []
for i in range(N):
    step.append(int(std()))

dp = [[0 for i in range(2)] for j in range(N)]

dp[0][0] = step[0]
if N >= 2:
    dp[1][0], dp[1][1] = step[1], step[0]+step[1]

for i in range(2, N):
    dp[i][0] = max(dp[i-2][1], dp[i-2][0]) + step[i]
    dp[i][1] = dp[i-1][0] + step[i]

print(max(dp[N-1]))
