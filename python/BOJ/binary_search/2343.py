from sys import stdin
from collections import deque

std = stdin.readline

N, M = map(int, std().split())
song = list(map(int, std().split()))

l, r = 1, 1000000000

answer = 1000000000

while l <= r:
    mid = (l+r) // 2
    lesson = 0
    bluelay = 0
    for i in range(N):
        if lesson+song[i] <= mid:
            lesson += song[i]
            if bluelay == 0:
                bluelay += 1
        else:
            lesson = 0
            if lesson+song[i] > mid:
                bluelay = -1
                break
            else:
                lesson += song[i]
                bluelay += 1

    if bluelay > M or bluelay == -1:  # 레슨 크기가 작아 블루레이가 더 필요할 때
        l = mid + 1
    else:
        answer = min(answer, mid)
        r = mid - 1

print(answer)
