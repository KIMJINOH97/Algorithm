from sys import stdin

std = stdin.readline

N, H = map(int, std().split())

obstacle = [0 for i in range(N)]

up, down = [], []
for i in range(N):
    if i % 2 == 0:
        down.append(int(std()))
    else:
        up.append(int(std()))

up.sort()
down.sort()

answer = [N+1, 0]

k = []
for i in range(1, H+1):
    down_cnt, up_cnt = 0, 0

    l, r = 0, len(down)-1
    # 아래에서 나오는 죽순
    while l <= r:
        mid = (l+r)//2
        if i <= down[mid]:  # 벽 부숨
            down_cnt = len(down)-mid
            r = mid-1
        else:
            l = mid+1

    l, r = 0, len(up)-1

    # 위에서 나오는 죽순
    while l <= r:
        mid = (l+r)//2
        if i > H-up[mid]:
            up_cnt = len(up) - mid
            r = mid-1

        else:
            l = mid+1

    ans = up_cnt + down_cnt
    if answer[0] == ans:
        answer[1] += 1
    elif ans < answer[0]:
        answer = [ans, 1]

print(*answer)
