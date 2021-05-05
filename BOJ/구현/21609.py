from sys import stdin
from collections import deque

std = stdin.readline

N, M = map(int, std().split())

board = []
for i in range(N):
    board.append(list(map(int, std().split())))

q, z = deque(), []
check = [[0 for i in range(N)] for j in range(N)]
nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]


def find_block(k):
    block, rain_block = [(q[0][0], q[0][1])], []
    while q:
        r, c = q.popleft()
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if dr < 0 or dc < 0 or dr >= N or dc >= N or check[dr][dc] == 1 or board[dr][dc] in [-1, -2]:
                continue
            if board[dr][dc] == 0:
                rain_block.append((dr, dc))
            elif board[dr][dc] != k:
                continue
            check[dr][dc] = 1
            if board[dr][dc] != 0:
                block.append((dr, dc))
            q.append((dr, dc))

    # 무지개 블럭 초기화
    for r in rain_block:
        r, c = r
        check[r][c] = 0

    # 기준 블럭 찾기 위함
    block = sorted(block, key=lambda x: (x[0], x[1]))
    if len(block)+len(rain_block) < 2:
        return -1
    # 기준 블럭 (r,c)와 block의 크기 반환
    return block[0][0], block[0][1], len(block)+len(rain_block), len(rain_block)


def zero(k):
    while z:
        r, c = z.pop(0)
        for i in range(4):
            dr, dc = r + nr[i], c + nc[i]
            if dr < 0 or dc < 0 or dr >= N or dc >= N or board[dr][dc] == -1:
                continue
            if board[dr][dc] != k and board[dr][dc] != 0:
                continue
            board[dr][dc] = -2
            z.append((dr, dc))


def down():
    new_board = [[-2 for i in range(N)]for i in range(N)]
    for j in range(N):
        base_r, base_c = N-1, j
        for i in range(N-1, -1, -1):
            # board[i][j] 순회
            if board[i][j] == -2:
                continue
            elif board[i][j] == -1:
                new_board[i][j] = -1
                base_r = i-1
            else:
                new_board[base_r][base_c] = board[i][j]
                base_r -= 1

    return new_board


def round():
    new_board = [[] for i in range(N)]
    for i in range(N):
        row = 0
        for j in range(N-1, -1, -1):
            new_board[row].append(board[i][j])
            row += 1

    return new_board


answer = 0
# 블럭의 기준, 사이즈 담는 배열
while True:
    all_block = []
    check = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if board[i][j] in [0, -1, -2] or check[i][j] == 1:
                continue
            check[i][j] = 1
            q.append((i, j))
            result = find_block(board[i][j])
            if result == -1:
                continue
            all_block.append(result)

    if len(all_block) == 0:
        break

    # 우선순위 1. 크기 2. 무지개 3. 행 4. 열
    all_block = sorted(all_block, key=lambda x: (-x[2], -x[3], -x[0], -x[1]))

    base_r, base_c, size, rainbow = all_block[0]
    z.append((base_r, base_c))
    zero(board[base_r][base_c])
    answer += size*size

    board = down()
    board = round()
    board = down()

print(answer)
