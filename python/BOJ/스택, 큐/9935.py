from sys import stdin
from itertools import combinations
from collections import deque

std = stdin.readline

str1 = std().rstrip()
boom = std().rstrip()
b_len = len(boom)

stack = []

same = 0
for i in range(len(str1)):
    if str1[i] == boom[same]:
        stack.append((str1[i], same))
        same += 1
        if same == b_len:
            for j in range(b_len):
                stack.pop()
            if stack and stack[-1][1] != -1:
                same = stack[-1][1] + 1
            else:
                same = 0
    else:
        same = 0
        if str1[i] == boom[same]:
            stack.append((str1[i], 0))
            same += 1
            if b_len == 1:
                stack.pop()
                same = 0
        else:
            stack.append((str1[i], -1))

if not stack:
    print("FRULA")
else:
    for s in stack:
        print(s[0], end="")
