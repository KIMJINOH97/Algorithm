from sys import stdin

std = stdin.readline

board = []
N = 19
for i in range(N):
    board.append(list(map(int, std().split())))

check = [[0 for i in range(N)] for j in range(N)]

nr, nc = [0, 1, 1, 1, 0, -1, -1, -1], [1, 1, 0, -1, -1, -1, 0, 1]

q = []

winner = 0
answer = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 0:
            continue

        count = [[] for i in range(8)]
        for k in range(8):
            cnt = 1
            while True:
                dr, dc = i+nr[k]*cnt, j+nc[k]*cnt
                if 0 <= dr < N and 0 <= dc < N and board[i][j] == board[dr][dc]:
                    count[k].append([dr, dc])
                    cnt += 1
                else:
                    break

        if len(count[0])+len(count[4])+1 == 5:
            winner = board[i][j]
            answer = count[0] + count[4] + [[i, j]]
            break
        if len(count[1])+len(count[5])+1 == 5:
            winner = board[i][j]
            answer = count[1] + count[5] + [[i, j]]
            break
        if len(count[2])+len(count[6])+1 == 5:
            winner = board[i][j]
            answer = count[2] + count[6] + [[i, j]]
            break
        if len(count[3])+len(count[7])+1 == 5:
            winner = board[i][j]
            answer = count[3] + count[7] + [[i, j]]
            break

    if winner != 0:
        break

answer = sorted(answer, key=lambda x: (x[1], x[0]))
if winner == 0:
    print("0")
else:
    print(winner)
    print(answer[0][0]+1, answer[0][1]+1)
