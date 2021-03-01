from sys import stdin

std = stdin.readline

N, K = map(int, std().split())
coin = []
dp = [0 for i in range(K+1)]

dp[0] = 1

for i in range(N):
    coin.append(int(std()))

for i, c in enumerate(coin):
    for j in range(K+1):
        if j-c >= 0:
            dp[j] += dp[j-c]

print(dp[K])
