def solution(t):
    answer = 0
    n = len(t)
    dp = [[0 for i in range(j+1)] for j in range(n)]
    dp[0][0] = t[0][0]
    for i in range(1, n):
        for j in range(i+1):
            if j-1 >= 0 and j < i:
                dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])+t[i][j]
            elif j-1 < 0:
                dp[i][j] += dp[i-1][j]+t[i][j]
            else:
                dp[i][j] += dp[i-1][j-1]+t[i][j]
    return max(map(max, dp))
