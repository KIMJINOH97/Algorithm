from sys import stdin

std = stdin.readline

N = int(std())

row = []

for i in range(N):
    row.append(list(map(int, std().split())))

dp = list(row[0])

ma, mi = max(dp), min(dp)


def solution():
    global dp, ma, mi
    for i in range(1, N):
        a, b, c = dp[0], dp[1], dp[2]
        dp[0] = max(a, b) + row[i][0]
        dp[1] = max(a, b, c) + row[i][1]
        dp[2] = max(b, c) + row[i][2]

    ma = max(dp)
    dp = row[0]
    for i in range(1, N):
        a, b, c = dp[0], dp[1], dp[2]
        dp[0] = min(a, b) + row[i][0]
        dp[1] = min(a, b, c) + row[i][1]
        dp[2] = min(b, c) + row[i][2]
    mi = min(dp)
    return ma, mi


solution()

print(ma, mi)
