from sys import stdin
from itertools import combinations
from collections import deque

std = stdin.readline

N = int(std())

top = list(map(int, std().split()))

receive = [0 for i in range(N)]

stack = []

for i in range(N-1, -1, -1):
    if len(stack) == 0:
        stack.append((top[i], i))
        continue
    if top[i] < stack[-1][0]:
        stack.append((top[i], i))
    else:
        while stack and stack[-1][0] <= top[i]:
            value, index = stack.pop()
            receive[index] = i+1
        stack.append((top[i], i))

print(*receive)
