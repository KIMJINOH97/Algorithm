def solution(board):
    answer = 0
    N = len(board)
    nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
    check = [[0 for i in range(N)] for j in range(N)]
    q = []

    def bfs():
        while q:
            r, c, d, s = q.pop(0)
            for i in range(4):
                dr, dc = r + nr[i], c + nc[i]
                if 0 <= dr < N and 0 <= dc < N and board[dr][dc] == 0:
                    if i % 2 != s % 2:
                        if check[dr][dc] == 0:
                            check[dr][dc] = d+600
                            q.append((dr, dc, d+600, i))
                        elif d+600 <= check[dr][dc]:
                            check[dr][dc] = d+600
                            q.append((dr, dc, d+600, i))
                    else:
                        if check[dr][dc] == 0:
                            check[dr][dc] = d+100
                            q.append((dr, dc, d+100, i))
                        elif d+100 <= check[dr][dc]:
                            check[dr][dc] = d+100
                            q.append((dr, dc, d+100, i))
        return check[N-1][N-1]

    if board[0][1] == 0:
        check[0][1] = 100
        q.append((0, 1, 100, 0))
    if board[1][0] == 0:
        check[1][0] = 100
        q.append((1, 0, 100, 1))
    answer = bfs()
    return answer
