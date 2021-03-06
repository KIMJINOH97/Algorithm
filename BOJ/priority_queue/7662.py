from sys import stdin
from heapq import heappop, heappush

std = stdin.readline

T = int(std())

answer, check = [], []


def q_pop(q):
    while q:
        a, b = heappop(q)
        if check[b] == 1:
            return (a, b)
    return -1


while T > 0:
    T -= 1
    N = int(std())

    min_q, max_q = [], []
    q_len = 0

    check = [0 for i in range(N)]
    for i in range(N):
        a, b = std().split()
        b = int(b)
        if a == 'I':
            heappush(min_q, (b, i))
            heappush(max_q, (-b, i))
            check[i] = 1
            q_len += 1
        else:
            if q_len == 0:
                continue
            if b == 1:
                num, index = q_pop(max_q)
            else:
                num, index = q_pop(min_q)
            check[index] = 0
            q_len -= 1

    if q_len == 0:
        answer.append("EMPTY")
    else:
        answer.append((-q_pop(max_q)[0], q_pop(min_q)[0]))

for a in answer:
    if a == "EMPTY":
        print(a)
    else:
        print(a[0], a[1])
