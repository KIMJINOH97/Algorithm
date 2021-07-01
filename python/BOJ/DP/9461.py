from sys import stdin

std = stdin.readline

T = int(std())

dp = [0 for _ in range(100)]

dp[0], dp[1], dp[2] = 1, 1, 1
dp[3], dp[4] = 2, 2
for i in range(5, 100):
    dp[i] = dp[i-5] + dp[i-1]

for i in range(T):
    a = int(std())
    print(dp[a-1])
