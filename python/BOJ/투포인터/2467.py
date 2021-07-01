from sys import stdin
from collections import deque

std = stdin.readline

N = int(std())


water = list(map(int, std().split()))

l, r = 0, N-1

answer = [water[l], water[r]]
sum_w = water[l]+water[r]

while l < r:
    if sum_w < 0:
        sum_w -= water[l]
        l += 1
        sum_w += water[l]
        if abs(sum_w) < abs(sum(answer)) and l != r:
            answer = [water[l], water[r]]
    else:
        sum_w -= water[r]
        r -= 1
        sum_w += water[r]
        if abs(sum_w) < abs(sum(answer)) and l != r:
            answer = [water[l], water[r]]

print(*answer)
