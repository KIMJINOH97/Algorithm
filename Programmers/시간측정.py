from sys import stdin
from collections import deque
from math import floor
import time

N = 100000
queue = [0 for i in range(N)]
deque = deque()
for i in range(N):
    deque.append(i)

start = time.time()
while queue:
    queue.pop(0)
end = time.time()
print(floor((end-start)*1000), "ms")

start = time.time()
while deque:
    deque.popleft()
end = time.time()
print(floor((end-start)*1000), "ms")
