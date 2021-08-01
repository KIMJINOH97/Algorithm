from sys import stdin

std = stdin.readline

N = int(std())

global answer
answer = 0
sand = []

for i in range(N):
    sand.append(list(map(int, std().split())))


nr, nc = [0, 1, 0, -1], [-1, 0, 1, 0]
sr, sc = [0, 1, 1, 1, 0, -1, -1, -1], [-1, -1, 0, 1, 1, 1, 0, -1]


def check(r, c):
    if r < 0 or c < 0 or r >= N or c >= N:
        return False
    return True


def twoDistance(r, c, ratio, sandWeight):
    global answer
    scatterSand = (sandWeight * ratio) // 100
    if check(r, c):
        sand[r][c] += scatterSand
    else:
        answer += scatterSand

    return scatterSand


def scatter(direct, r, c):  # y의 방향과 좌표
    global answer
    dr, dc = r + 2 * nr[direct], c + 2 * nc[direct]
    left_dr, left_dc = r + 2 * nr[(direct + 1) %
                                  4], c + 2 * nc[(direct + 1) % 4]
    right_dr, right_dc = r + 2 * \
        nr[(direct + 3) % 4], c + 2 * nc[(direct + 3) % 4]

    sumOfScatter = 0

    sumOfScatter += twoDistance(dr, dc, 5, sand[r][c])
    sumOfScatter += twoDistance(left_dr, left_dc, 2, sand[r][c])
    sumOfScatter += twoDistance(right_dr, right_dc, 2, sand[r][c])

    persant = [0, 10, 7, 1, 0, 1, 7, 10]
    for i in range(1, 8):
        d = (direct * 2 + i) % 8
        dr, dc = r + sr[d], c + sc[d]
        sumOfScatter += twoDistance(dr, dc, persant[i], sand[r][c])

    remain = sand[r][c] - sumOfScatter
    dr, dc = r + nr[direct], c + nc[direct]
    if check(dr, dc):
        sand[dr][dc] += remain
    else:
        answer += remain

    sand[r][c] = 0


def tor():
    t_r, t_c = (N-1) // 2, (N-1) // 2
    cnt = 0
    while True:
        for i in range(4):
            if i % 2 == 0:
                cnt += 1

            for j in range(cnt):
                t_r, t_c = t_r + nr[i], t_c + nc[i]
                scatter(i, t_r, t_c)
                if t_r == 0 and t_c == 0:
                    return


tor()

print(answer)
