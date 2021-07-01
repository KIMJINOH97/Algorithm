from sys import stdin
from heapq import heappop, heappush

std = stdin.readline

N = int(std())

h = []
for i in range(N):
    heappush(h, int(std()))

ans = 0
while len(h) > 1:
    card1 = heappop(h)
    card2 = heappop(h)
    ans += card1+card2
    heappush(h, card1+card2)

print(ans)
