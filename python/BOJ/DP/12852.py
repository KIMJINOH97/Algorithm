from sys import stdin

std = stdin.readline

N = int(std())

dp = [100000 for i in range(N+1)]
dp[1] = 0
dic = {i: [] for i in range(N+1)}
dic[1].append(1)
for i in range(1, N):
    two, three, plus = i*3, i*2, i+1
    if three <= N:
        if dp[i]+1 < dp[three]:
            dp[three] = dp[i]+1
            dic[three] = [three] + dic[i]
    if two <= N:
        if dp[i]+1 < dp[two]:
            dp[two] = dp[i]+1
            dic[two] = [two] + dic[i]
    if plus <= N:
        if dp[i]+1 < dp[plus]:
            dp[plus] = dp[i]+1
            dic[plus] = [plus] + dic[i]
print(dp[N])
print(*dic[N])
