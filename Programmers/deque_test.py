from sys import stdin, getsizeof
from collections import deque
from math import floor
import time

N = 10000


start = time.time()
queue = [0 for i in range(N)]
end = time.time()
print("10000개 넣은 list: ", floor((end-start)*10000), "ms")


start = time.time()
deque = deque()
for i in range(N):
    deque.append(i)
end = time.time()
print("10000개 넣은 deque: ", floor((end-start)*10000), "ms")

# li = []
# print("빈 리스트 : ", getsizeof(li))
# for i in range(10):
#     li.append(0)
#     print(i+1, "번째 원소 삽입 후 크기: ", getsizeof(li))
