from sys import stdin

std = stdin.readline

gear = []

# 12시 부터 저장
for i in range(4):
    gear.append(list(map(int, list(std().rstrip()))))

# 3시 index : 2, 9시 index = 6
three_clock, nine_clock = 2, 6

K = int(std())


def rotate_clock(n):
    global gear
    pre = gear[n][7]
    for i in range(8):
        tmp = gear[n][i]
        gear[n][i] = pre
        pre = tmp


def rotate_unclock(n):
    global gear
    first = gear[n][0]
    for i in range(7):
        gear[n][i] = gear[n][i+1]
    gear[n][7] = first


def rotate(num, direction):
    global gear
    cnt = 0

    left_rotate, right_rotate = num, num
    direct = [0 for i in range(4)]
    direct[num] = direction

    while True:
        if left_rotate - 1 < 0:
            break
        left_rotate -= 1

        if gear[left_rotate][three_clock] == gear[left_rotate+1][nine_clock]:
            break
        else:
            if direct[left_rotate+1] == 1:
                direct[left_rotate] = -1
            else:
                direct[left_rotate] = 1

    while True:
        if right_rotate + 1 > 3:
            break

        right_rotate += 1

        if gear[right_rotate][nine_clock] == gear[right_rotate - 1][three_clock]:
            break
        else:
            if direct[right_rotate-1] == 1:
                direct[right_rotate] = -1
            else:
                direct[right_rotate] = 1

    for i in range(4):
        if direct[i] == 0:
            continue
        elif direct[i] == 1:
            rotate_clock(i)
        else:
            rotate_unclock(i)

    return


answer = 0

for i in range(K):
    num, direction = map(int, std().split())
    rotate(num-1, direction)

score = 1
for i in range(4):
    if gear[i][0] == 1:
        answer += score
    score *= 2

print(answer)
