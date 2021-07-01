from sys import stdin

std = stdin.readline

N = int(std())

chair = [[-1 for j in range(N)] for i in range(N)]
priority = [[] for i in range(N*N)]


nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]


def check(st_num):
    empty = [[[0, 0] for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            if chair[i][j] != -1:
                continue
            for k in range(4):
                dr, dc = i+nr[k], j+nc[k]
                if dr >= N or dc >= N or dr < 0 or dc < 0:
                    continue

                if chair[dr][dc] == -1:
                    empty[i][j][0] += 1
                elif chair[dr][dc] in priority[st_num]:
                    empty[i][j][1] += 1

    sort_empty = []
    for i in range(N):
        for j in range(N):
            if chair[i][j] != -1:
                continue
            em, pr = empty[i][j]
            sort_empty.append((em, pr, i, j))

    sort_empty = sorted(sort_empty, key=lambda x: (-x[1], -x[0], x[2], x[3]))
    em, pr, r, c = sort_empty[0]
    chair[r][c] = st_num
    return sort_empty[0]


def sum_ans():
    ans = 0
    for i in range(N):
        for j in range(N):
            student = chair[i][j]
            cnt = 0
            for k in range(4):
                dr, dc = i+nr[k], j+nc[k]
                if dr < 0 or dc < 0 or dr >= N or dc >= N:
                    continue
                if chair[dr][dc] in priority[student]:
                    cnt += 1
            if cnt == 0:
                continue
            else:
                ans += pow(10, cnt-1)
    return ans


for i in range(N*N):
    k = list(map(lambda x: int(x) - 1, std().split()))
    student = k[0]
    priority[k[0]] = k[1:]
    check(student)

print(sum_ans())
