from sys import stdin
from heapq import heappop, heappush

std = stdin.readline

N = int(std())

maxHeap, minHeap = [], []  # max 작은것 minHeap에는 큰것 대입 그래야 중앙값 찾을 수 있음.

num = []
for i in range(N):
    num.append(int(std()))

answer = []


def soluntion():
    answer.append(num[0])

    if N == 1:
        return

    maxHeapStart, minHeapStart = min(num[0], num[1]), max(num[0], num[1])
    heappush(maxHeap, -maxHeapStart)
    heappush(minHeap, minHeapStart)

    answer.append(maxHeapStart)

    for i in range(2, N):
        if num[i] > minHeap[0]:
            heappush(minHeap, num[i])
        else:
            heappush(maxHeap, -num[i])

        maxLen, minLen = len(maxHeap), len(minHeap)

        if maxLen > minLen:
            heappush(minHeap, -heappop(maxHeap))
        elif minLen > maxLen + 1:
            heappush(maxHeap, -heappop(minHeap))

        maxLen, minLen = len(maxHeap), len(minHeap)
        if minLen == maxLen:
            answer.append(min(-maxHeap[0], minHeap[0]))
        else:
            answer.append(minHeap[0])


soluntion()

for i in range(N):
    print(answer[i])
