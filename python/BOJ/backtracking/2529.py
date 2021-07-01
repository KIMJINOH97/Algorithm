from sys import stdin
from itertools import permutations

std = stdin.readline

N = int(std())
bu = list(std().split())

answer = []
check = [0 for i in range(10)]
c = []


def back():
    if len(c) == N+1:
        for i in range(len(bu)):
            if bu[i] == '<':
                if c[i] >= c[i+1]:
                    break
            else:
                if c[i] <= c[i+1]:
                    break
        else:
            answer.append(''.join(list(map(str, c))))
        return

    for i in range(10):
        if check[i] == 0:
            check[i] = 1
            c.append(i)
            back()
            check[i] = 0
            c.pop()


back()
answer = sorted(answer, key=lambda x: int(x))
print(answer[-1])
print(answer[0])
