def solution(board):
    answer = 0
    col, row = len(board[0]), len(board)
    dp = [[0 for i in range(col)] for j in range(row)]

    for i, bo in enumerate(board):
        for j, b in enumerate(bo):
            if b == 0:
                continue
            if 0 <= i-1 < row and 0 <= j-1 < col:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = 1
    answer = max(map(max, dp))

    return answer*answer
