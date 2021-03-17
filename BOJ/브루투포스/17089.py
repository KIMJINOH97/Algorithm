from sys import stdin
from itertools import combinations
from collections import deque

std = stdin.readline

N, M = map(int, std().split())
friend = [[]for i in range(N)]
answer = 20000
for i in range(M):
    a, b = map(int, std().split())
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)

for i in range(N):
    if len(friend[i]) < 2:
        continue
    A = friend[i]
    for fr in combinations(A, 2):
        B, C = fr
        friend_sum = 0
        if C in friend[B]:
            friend_sum = len(A)+len(friend[B])+len(friend[C]) - 6
            if friend_sum < answer:
                answer = friend_sum

print(answer if answer != 20000 else -1)
