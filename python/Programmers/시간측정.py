from sys import stdin
from collections import deque
from math import floor
import time

N = 1000000
queue = [0 for i in range(N)]
deque = deque()
for i in range(N):
    deque.append(i)

# start = time.time()
# for i in range(10000):
#     del queue[1000]
# end = time.time()
# print(floor((end-start)*1000), "ms")

start = time.time()
for i in range(200000):
    deque.insert(10000, 1)
end = time.time()
print(floor((end-start)*1000), "ms")
