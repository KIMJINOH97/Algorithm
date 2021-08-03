from itertools import permutations
from copy import deepcopy
from collections import deque


def solution(board, c_r, c_c):
    answer = []
    N = 4
    check, dist = [], []
    nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]

    numDic = {key: [] for key in range(7)}
    for i in range(N):
        for j in range(N):
            if board[i][j] != 0:
                check.append(board[i][j])
                numDic[board[i][j]].append((i, j))

    card = list(set(check))
    orders = list(permutations(card, len(card)))

    q = deque()

    def checkDist(r, c, d, dist):
        if dist[r][c] == -1 or d + 1 < dist[r][c]:
            dist[r][c] = d + 1
            q.append((r, c, d + 1))
        return None

    def bfs(cardBoard, start_r, start_c):
        q.append((start_r, start_c, 0))
        dist = [[-1 for i in range(N)] for j in range(N)]
        dist[start_r][start_c] = 0
        while q:
            r, c, d = q.popleft()
            for i in range(4):
                dr, dc = r + nr[i], c + nc[i]
                if dr < 0 or dc < 0 or dr >= N or dc >= N:
                    continue

                checkDist(dr, dc, d, dist)

                if cardBoard[dr][dc] != 0:
                    continue

                # ctrl 누른 뒤
                ct_r, ct_c = -1, -1
                for j in range(2, 4):
                    dr, dc = r + j * nr[i], c + j * nc[i]
                    if dr < 0 or dc < 0 or dr >= N or dc >= N:
                        break

                    if cardBoard[dr][dc] != 0:
                        ct_r, ct_c = dr, dc
                        break
                    ct_r, ct_c = dr, dc

                if ct_r != -1:
                    checkDist(ct_r, ct_c, d, dist)

        return dist

    def dfs(order, board, ans, depth, r, c):
        if depth == len(card):
            answer.append(ans)
            return

        findCard = order[depth]
        (f1_r, f1_c), (f2_r, f2_c) = numDic[findCard]
        # f1_r, f1_c = findCard1
        # f2_r, f2_c = findCard2

        new_board1, new_board2 = deepcopy(board), deepcopy(board)
        new_board1[f1_r][f1_c] = 0
        new_board1[f2_r][f2_c] = 0
        new_board2[f1_r][f1_c] = 0
        new_board2[f2_r][f2_c] = 0

        dist = bfs(board, r, c)
        first, second = ans + dist[f1_r][f1_c], ans + dist[f2_r][f2_c]

        dist = bfs(board, f1_r, f1_c)
        first += dist[f2_r][f2_c]

        dist = bfs(board, f2_r, f2_c)
        second += dist[f1_r][f1_c]

        dfs(order, new_board1, first + 2, depth + 1, f2_r, f2_c)
        dfs(order, new_board2, second + 2, depth + 1, f1_r, f1_c)

    if board[c_r][c_c] != 0:
        orders = list(filter(lambda x: x[0] == board[c_r][c_c], orders))

    for order in orders:
        dfs(order, board, 0, 0, c_r, c_c)

    return min(answer)
