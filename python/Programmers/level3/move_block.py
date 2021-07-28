from collections import deque


def solution(board):
    answer = 0

    N, GARO, SERO = len(board), 0, 1
    nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]

    q = deque()
    q.append(([(0, 0), (0, 1)], 0, GARO))

    sero_dist = [[0 for i in range(N)] for j in range(N)]
    garo_dist = [[0 for i in range(N)] for j in range(N)]

    def checkRange(r, c):
        return False if r < 0 or r >= N or c < 0 or c >= N else True

    def checkBlock(r, c):
        return False if board[r][c] else True

    def checkBlockAndRange(fr, fc, sr, sc):
        if not checkRange(fr, fc) or not checkRange(sr, sc):
            return False

        if not checkBlock(fr, fc) or not checkBlock(sr, sc):
            return False

        return True

    def checkDist(location, direct, distance):
        r, c = location
        if direct == GARO:
            if garo_dist[r][c] == 0 or garo_dist[r][c] > distance + 1:
                garo_dist[r][c] = distance + 1
                return True
            return False

        if sero_dist[r][c] == 0 or sero_dist[r][c] > distance + 1:
            sero_dist[r][c] = distance + 1
            return True
        return False

    def rotateGaro(location, d):
        fr, fc = location[0]
        sr, sc = location[1]
        up_dr, up_dc, down_dr, down_dc = sr - 1, sc - 1, sr + 1, sc - 1

        # 오른쪽 정점 기준
        if checkBlockAndRange(up_dr, up_dc, fr, fc):  # 오른쪽 정점 왼쪽위로 돌림
            if board[up_dr][up_dc+1] == 0 and checkDist([fr, fc], SERO, d):
                q.append(([(up_dr, up_dc), location[0]], d+1, SERO))

        if checkBlockAndRange(fr, fc, down_dr, down_dc):
            if board[down_dr][down_dc+1] == 0 and checkDist([down_dr, down_dc], SERO, d):
                q.append(([location[0], (down_dr, down_dc)], d+1, SERO))

        up_dr, up_dc, down_dr, down_dc = fr - 1, fc + 1, fr + 1, fc + 1

        # 왼쪽 정점 기준
        if checkBlockAndRange(up_dr, up_dc, sr, sc):
            if board[up_dr][up_dc-1] == 0 and checkDist([sr, sc], SERO, d):
                q.append(([(up_dr, up_dc), location[1]], d+1, SERO))

        if checkBlockAndRange(sr, sc, down_dr, down_dc):
            if board[down_dr][down_dc-1] == 0 and checkDist([down_dr, down_dc], SERO, d):
                q.append(([location[1], (down_dr, down_dc)], d+1, SERO))

    def rotateSero(location, d):
        fr, fc = location[0]
        sr, sc = location[1]
        left_dr, left_dc, right_dr, right_dc = fr + 1, fc - 1, fr + 1, fc + 1

        # 위에꺼 이동
        if checkBlockAndRange(left_dr, left_dc, sr, sc):
            if board[left_dr-1][left_dc] == 0 and checkDist([sr, sc], GARO, d):
                q.append(([(left_dr, left_dc), location[1]], d+1, GARO))

        if checkBlockAndRange(right_dr, right_dc, sr, sc):
            if board[right_dr-1][right_dc] == 0 and checkDist([right_dr, right_dc], GARO, d):
                q.append(([location[1], (right_dr, right_dc)], d+1, GARO))

        left_dr, left_dc, right_dr, right_dc = sr - 1, sc - 1, sr - 1, sc + 1

        # 아래꺼 이동
        if checkBlockAndRange(left_dr, left_dc, fr, fc):
            if board[left_dr+1][left_dc] == 0 and checkDist([fr, fc], GARO, d):
                q.append(([(left_dr, left_dc), location[0]], d+1, GARO))

        if checkBlockAndRange(right_dr, right_dc, fr, fc):
            if board[right_dr+1][right_dc] == 0 and checkDist([right_dr, right_dc], GARO, d):
                q.append(([location[0], (right_dr, right_dc)], d+1, GARO))
        return

    while q:
        location, d, direct = q.popleft()
        first_r, first_c = location[0]
        second_r, second_c = location[1]

        for i in range(4):
            first_dr, first_dc = first_r + nr[i], first_c + nc[i]
            second_dr, second_dc = second_r + nr[i], second_c + nc[i]

            if not checkBlockAndRange(first_dr, first_dc, second_dr, second_dc):
                continue

            move = [(first_dr, first_dc), (second_dr, second_dc)]
            move.sort()

            if not checkDist(move[-1], direct, d):
                continue

            q.append((move, d+1, direct))

        if direct == GARO:
            rotateGaro(location, d)
        else:
            rotateSero(location, d)

    garo, sero = garo_dist[N-1][N-1], sero_dist[N-1][N-1]

    if garo == 0:
        answer = sero
    elif sero == 0:
        answer = garo
    else:
        answer = min(garo, sero)

    return answer
