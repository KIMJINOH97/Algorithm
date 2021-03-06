from sys import stdin


std = stdin.readline

N, M = map(int, std().split())

chess = []

white = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], [
    'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

black = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], [
    'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'], ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'], ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]


for i in range(N):
    chess.append(list(std().rstrip()))


def check_white(r, c):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if white[i][j] != chess[r+i][c+j]:
                cnt += 1
    return cnt


def check_black(r, c):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if black[i][j] != chess[r+i][c+j]:
                cnt += 1
    return cnt


answer = 2500
for i in range(N-8+1):
    for j in range(M-8+1):
        w, b = check_black(i, j), check_white(i, j)
        answer = min(w, b, answer)

print(answer)
