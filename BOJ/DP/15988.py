from sys import stdin

std = stdin.readline

T = int(std())

test = []
while T > 0:
    T -= 1
    test.append(int(std()))

max_test = max(test)
dp = [0 for i in range(max_test+1)]

dp[0], dp[1] = 1, 1
if max_test >= 2:
    dp[2] = 2

for i in range(3, max_test+1):
    dp[i] = (dp[i-1] % 1000000009+dp[i-2] %
             1000000009+dp[i-3] % 1000000009) % 1000000009

for t in test:
    print(dp[t])
