from sys import stdin, getsizeof
from collections import deque
from math import floor
import time

N = 1000000


start = time.time()
queue = [0 for i in range(N)]
end = time.time()
print(N, "개 넣은 list <append(i)>: ", floor((end-start)*10000), "ms")


start = time.time()
dq = deque()
for i in range(N):
    dq.append(i)
end = time.time()
print(N, "개 넣은 deque <append(i)>: ", floor((end-start)*10000), "ms")

li = []

for i in range(N):
    li.append(i)

start = time.time()
while li:
    li.pop()

end = time.time()

print(N, "개 pop 한 list: ", floor((end-start)*10000), "ms")


dq = deque()

for i in range(N):
    dq.appendleft(i)

start = time.time()

while dq:
    dq.popleft()

end = time.time()
print(N, "개 popleft 한 deque: ", floor((end-start)*10000), "ms")


# li = []
# print("빈 리스트 : ", getsizeof(li))
# for i in range(10):
#     li.append(0)
#     print(i+1, "번째 원소 삽입 후 크기: ", getsizeof(li))


start = time.time()

for i in range(N):
    li.append(i)

end = time.time()

print(N, "개 append한 list: ", floor((end-start)*10000), "ms")


start = time.time()

for i in range(N):
    dq.appendleft(i)

end = time.time()
print(N, "개 appendleft 한 deque: ", floor((end-start)*10000), "ms")

start = time.time()
