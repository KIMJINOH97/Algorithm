def solution(dirs):
    answer = 0
    N = 11
    board = [[[0, 0, 0, 0] for j in range(N)] for i in range(N)]
    dot_r, dot_c = 5, 5
    dic = {'U': 3, 'D': 1, 'R': 0, 'L': 2}
    nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]

    cnt = 0
    for d in dirs:
        i = dic[d]
        dr, dc = dot_r+nr[i], dot_c+nc[i]
        if dr < 0 or dc < 0 or dr >= N or dc >= N:
            continue

        if board[dr][dc][(i-2) % 4] == 0:
            board[dot_r][dot_c][i] = 1
            board[dr][dc][(i-2) % 4] = 1
            cnt += 1
        dot_r, dot_c = dr, dc

    return cnt
