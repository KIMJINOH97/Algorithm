from sys import stdin

std = stdin.readline

N, M, k = map(int, std().split())

sea = [[[]for i in range(N)] for j in range(N)]
shark = [[] for i in range(M)]  # row, column, direction
smell = [[[]for i in range(N)] for i in range(N)]

for i in range(N):
    s = list(map(int, std().split()))
    for j in range(N):
        if s[j] != 0:
            num = s[j]
            shark[num-1] = [i, j, s[j]-1, 0]
            sea[i][j].append(num-1)

direct = list(map(lambda x: int(x) - 1, std().split()))

for i, d in enumerate(direct):
    shark[i][3] = d

shark_priority = [[] for i in range(M)]

nr, nc = [-1, 1, 0, 0], [0, 0, -1, 1]  # 위 아래 왼 오

for i in range(M*4):
    shark_priority[i//4].append(list(map(lambda x: int(x)-1, std().split())))


def remain_smell(time):
    for i in range(len(shark)):
        r, c, num, d = shark[i]
        smell[r][c] = [num, time]


def reduce_smell():
    for i in range(N):
        for j in range(N):
            if len(smell[i][j]) > 0:
                smell[i][j][1] -= 1
                if smell[i][j][1] == 0:
                    smell[i][j] = []


def move_shark():
    global shark
    dic = {}  # 상어 모음
    for i in range(len(shark)):
        # 빈 자리 있는지 확인
        r, c, num, d = shark[i]
        priority = shark_priority[num][d]  # i번 상어가 d방향을 볼 때 우선순위
        flag = 0
        me_r, me_c = 0, 0
        for p in priority:
            dr, dc = r+nr[p], c+nc[p]
            if 0 <= dr < N and 0 <= dc < N:
                if len(smell[dr][dc]) == 0:  # 냄새가 빈자리로 이동
                    if (dr, dc) not in dic:
                        dic[(dr, dc)] = [(num, p)]
                    else:
                        dic[(dr, dc)].append((num, p))
                    flag = 1
                    break
                elif flag == 0 and smell[dr][dc][0] == num:  # 내가 있는 흔적 남김
                    flag = 2
                    me_r, me_c, me_num, me_d = dr, dc, num, p

        if flag == 2:
            if (me_r, me_c) not in dic:
                dic[(me_r, me_c)] = [(me_num, me_d)]
            else:
                dic[(me_r, me_c)].append((me_num, me_d))

    shark = []

    for key in dic:
        row, column = key
        if len(key) > 1:
            dic[key].sort()
            dic[key] = [dic[key][0]]
        shark.append([row, column, dic[key][0][0], dic[key][0][1]])


t = 0
while True:
    t += 1
    remain_smell(k)
    move_shark()
    reduce_smell()

    if t > 1000 or len(shark) == 1:
        break

print(t if t != 1001 else -1)
