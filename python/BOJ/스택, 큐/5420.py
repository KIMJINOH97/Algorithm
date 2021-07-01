from sys import stdin
from collections import deque

std = stdin.readline

T = int(std())

answer = []
for i in range(T):
    d = deque()
    str1 = std()
    N = int(std())
    a = std().rstrip()[1:-1]
    if N > 0:
        d = deque(map(int, a.split(',')))

    ans, flag = '', False
    for s in str1:
        if s == 'D' and len(d) == 0:
            ans = 'error'
            break
        if s == 'D' and flag == False:
            d.popleft()
        elif s == 'D' and flag == True:
            d.pop()
        elif s == 'R':
            flag = not flag

    if not ans == 'error':
        if flag == False:
            answer.append(list(d))
        else:
            k = []
            while d:
                k.append(d.pop())
            answer.append(k)
    else:
        answer.append(ans)

for a in answer:
    if a == 'error':
        print(a)
        continue
    print('[', end="")
    for i in range(len(a)):
        if i == len(a)-1:
            print(a[i], end="")
        else:
            print(a[i], end=",")
    print(']')
