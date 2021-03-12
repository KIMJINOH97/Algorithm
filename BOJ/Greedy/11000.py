from sys import stdin
from heapq import heappop, heappush

std = stdin.readline

N = int(std())

lec = []
for i in range(N):
    lec.append(tuple(map(int, std().split())))


q = []

lec.sort()
answer = 0

for i, l in enumerate(lec):
    start, end = l
    if len(q) == 0:
        heappush(q, (end, start))
    else:
        if start < q[0][0]:
            heappush(q, (end, start))
        else:
            while len(q) > 0 and start >= q[0][0]:
                heappop(q)
            heappush(q, (end, start))

    if len(q) > answer:
        answer = len(q)

print(answer)
