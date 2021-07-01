from sys import stdin
from heapq import heappop, heappush

N = int(stdin.readline())
hq = []
for i in range(N):
    K = int(stdin.readline())
    if K == 0:
        if len(hq) == 0:
            print("0")
        else:
            print(heappop(hq))
    else:
        heappush(hq, K)
