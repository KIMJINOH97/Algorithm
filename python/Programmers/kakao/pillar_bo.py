def solution(N, build_frame):
    answer = []

    GI, BO = 0, 1
    RM, UP = 0, 1
    N += 1

    board = [[[0, 0] for i in range(N)] for j in range(N)]

    def check():
        for i in range(N):
            for j in range(N):
                if board[i][j][GI] == UP:
                    result = checkPillar(i, j)
                    if not result:
                        return False

                if board[i][j][BO] == UP:
                    result = checkBo(i, j)
                    if not result:
                        return False

        return True

    def checkPillar(r, c):
        # 맨 밑에 있을 때
        if r == N-1:
            return True

        # 다른 기둥이 밑에 있어 세워질 때
        if r + 1 < N and board[r+1][c][GI] == UP:
            return True

        # 보 위에 기둥 세워 졌을 때
        if c - 1 >= 0 and board[r][c-1][BO] == UP:
            return True

        # 보 위에 기둥 세워 졌을 때
        if board[r][c][BO] == UP:
            return True

        return False

    def checkBo(r, c):
        # 보의 왼쪽에 기둥이 세워 졌을 때
        if board[r+1][c][GI] == UP:
            return True

        # 보의 오른쪽에 기둥이 세워졌을 때
        if board[r+1][c+1][GI] == UP:
            return True

        # 왼쪽에 보가 있는지 판단
        if c - 1 >= 0 and board[r][c-1][BO] == UP:
            # 오른쪽에도 보가 있는지 판단
            if c + 1 < N and board[r][c+1][BO] == UP:
                return True

        return False

    for x, y, a, b in build_frame:
        r, c = (N-1)-y, x

        # a -> 기둥 or 보  b -> 제거 or 세우기
        board[r][c][a] = b

        result = check()

        if not result and b == UP:
            board[r][c][a] = RM
        elif not result and b == RM:
            board[r][c][a] = UP

    for i in range(N):
        for j in range(N):
            if board[i][j][GI] == 1:
                answer.append([j, N-1-i, GI])
            if board[i][j][BO] == 1:
                answer.append([j, N-1-i, BO])

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))
