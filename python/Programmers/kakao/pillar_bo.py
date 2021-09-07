def solution(n, build_frame):
    answer = []
    PILLAR, BO = 0, 1
    board = [[[0, 0] for i in range(n+1)] for j in range(n+1)]

    def upPillar(r, c):
        if checkPillar(r, c):
            board[r][c][PILLAR] = 1
        return

    def checkPillar(r, c):
        if r == n or board[r+1][c][PILLAR]:
            return True

        if (c-1 >= 0 and board[r][c-1][BO]) or board[r][c][BO]:
            return True

        return False

    def checkBo(r, c):
        if c-1 >= 0 and c+1 <= n:
            if board[r][c-1][BO] and board[r][c+1][BO]:
                return True

        if board[r+1][c][PILLAR] or board[r+1][c+1][PILLAR]:
            return True

        return False

    def removePillar(r, c):
        board[r][c][PILLAR] = 0

        for i in range(n+1):
            for j in range(n+1):
                if board[i][j][BO] and not checkBo(i, j):
                    board[r][c][PILLAR] = 1
                    return
                if board[i][j][PILLAR] and not checkPillar(i, j):
                    board[r][c][PILLAR] = 1
                    return
        return

    def addBo(r, c):
        if checkBo(r, c):
            board[r][c][BO] = 1
        return

    def removeBo(r, c):

        board[r][c][BO] = 0

        for i in range(n+1):
            for j in range(n+1):
                if board[i][j][PILLAR]:
                    if not checkPillar(i, j):
                        board[r][c][BO] = 1
                        return
                if board[i][j][BO]:
                    if not checkBo(i, j):
                        board[r][c][BO] = 1
                        return

        return

    for x, y, a, b in build_frame:  # a (0: 기둥, 1: 보) b (0: 삭제, 1: 설치)
        c, r = x, n - y
        if a == PILLAR:
            if b == 1:
                upPillar(r, c)
            else:
                removePillar(r, c)
        else:
            if b == 1:
                addBo(r, c)
            else:
                removeBo(r, c)

    for i in range(n+1):
        for j in range(n+1):
            for k in range(2):
                if board[i][j][k] == 1:
                    answer.append([j, n-i, k])

    return sorted(answer, key=lambda x: (x[0], x[1], x[2]))
