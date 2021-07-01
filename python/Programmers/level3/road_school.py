def solution(m, n, puddles):
    answer = 0
    dp = [[0 for i in range(m)] for j in range(n)]
    dp[0][0] = 1

    for puddle in puddles:
        dp[puddle[1]-1][puddle[0]-1] = -1

    for i in range(n):
        for j in range(m):
            if dp[i][j] == -1:
                continue
            if 0 <= i-1 and 0 <= j-1:
                if dp[i-1][j] != -1:
                    dp[i][j] += dp[i-1][j]
                if dp[i][j-1] != -1:
                    dp[i][j] += dp[i][j-1]
            elif 0 <= i-1 and dp[i-1][j] != -1:
                dp[i][j] = dp[i-1][j]
            elif 0 <= j-1 and dp[i][j-1] != -1:
                dp[i][j] = dp[i][j-1]

    return dp[n-1][m-1] % 1000000007
