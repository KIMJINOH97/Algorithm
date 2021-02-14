from sys import stdin
from copy import deepcopy

box = [[] for i in range(4)]
fish = [[] for i in range(16)]

for i in range(4):
    a = list(map(int, stdin.readline().split()))
    for j in range(0, 8, 2):
        box[i].append([a[j]-1, a[j+1]-1])
        fish[a[j]-1] = [i, j//2]

# 상어 첫번째 식사
shark_d = box[0][0][1]
fish[box[0][0][0]] = []
answer = box[0][0][0]+1
box[0][0] = [-1, shark_d]
nr, nc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, -1, -1, -1, 0, 1, 1, 1]


def fish_move():
    for i in range(16):  # 물고기 개수만큼 순회
        if fish[i] == []:
            continue
        # 회전 물고기
        f_r, f_c = fish[i]
        f_d = box[f_r][f_c][1]
        for j in range(9):
            direction = (f_d + j) % 8
            dr, dc = f_r + nr[direction], f_c + nc[direction]
            if 0 <= dr < 4 and 0 <= dc < 4 and not box[dr][dc][0] == -1:
                box[f_r][f_c][1] = direction
                if box[dr][dc][0] == -2:
                    fish[i] = [dr, dc]
                else:
                    fish[i], fish[box[dr][dc][0]] = [dr, dc], fish[i]
                box[f_r][f_c], box[dr][dc] = box[dr][dc], box[f_r][f_c]
                break


def shark_eat(s_r, s_c, s_d, ans, depth):
    global answer, box, fish
    fish_move()
    temp_b, temp_f = deepcopy(box), deepcopy(fish)
    for i in range(1, 4):
        dr, dc = s_r+nr[s_d]*i, s_c+nc[s_d]*i
        if 0 <= dr < 4 and 0 <= dc < 4 and box[dr][dc][0] >= 0:
            box[s_r][s_c][0] = -2  # 상어위치 빈 공간
            eat = box[dr][dc][0]  # 먹이
            box[dr][dc] = [-1, box[dr][dc][1]]  # 다음 상어 대입
            fish[eat] = []
            shark_eat(dr, dc, box[dr][dc][1], ans+eat+1, depth+1)
            box, fish = deepcopy(temp_b), deepcopy(temp_f)

    if answer < ans:
        answer = ans
        return


shark_eat(0, 0, shark_d, answer, 0)
print(answer)
