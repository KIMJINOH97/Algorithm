def solution(R, C, queries):
    answer = []
    board = [[j*C+1+i for i in range(C)] for j in range(R)]

    def change(r1, c1, r2, c2):
        tmp = board[r1+1][c1]
        ans = []
        for j in range(c1, c2):  # 오른쪽
            tmp2 = board[r1][j]
            board[r1][j] = tmp
            tmp = tmp2
            ans.append(tmp)

        for i in range(r1, r2):
            tmp2 = board[i][c2]
            board[i][c2] = tmp
            tmp = tmp2
            ans.append(tmp)

        for j in range(c2, c1, -1):
            tmp2 = board[r2][j]
            board[r2][j] = tmp
            tmp = tmp2
            ans.append(tmp)

        for i in range(r2, r1, -1):
            tmp2 = board[i][c1]
            board[i][c1] = tmp
            tmp = tmp2
            ans.append(tmp)

        return min(ans)

    for query in queries:
        r1, c1, r2, c2 = map(lambda x: int(x) - 1, query)
        answer.append(change(r1, c1, r2, c2))

    return answer
