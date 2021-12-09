from heapq import heappop, heappush


def solution(K, A):
    MAX_VALUE = 1000000000
    if K < 0:
        return 0
    global firstIndex, lastIndex
    firstIndex, lastIndex = 0, 0
    N = len(A)

    answer = 0
    maxHeap, minHeap = [-A[0]], [A[0]]
    dic = {}
    dic[A[0]] = 1

    def findNewStart():
        global firstIndex, lastIndex
        dic[A[firstIndex]] -= 1
        firstIndex += 1

        while maxHeap and dic[-maxHeap[0]] == 0:
            heappop(maxHeap)

        while minHeap and dic[minHeap[0]] == 0:
            heappop(minHeap)

        while (-maxHeap[0]) - minHeap[0] > K:
            dic[A[lastIndex]] -= 1
            lastIndex -= 1

            while maxHeap and dic[-maxHeap[0]] == 0:
                heappop(maxHeap)

            while minHeap and dic[minHeap[0]] == 0:
                heappop(minHeap)

            # print("new", firstIndex, lastIndex)

    while firstIndex < N - 1:
        # print(firstIndex, lastIndex, "1111111111")

        if (-maxHeap[0]) - minHeap[0] <= K and lastIndex < N:
            lastIndex += 1
            if lastIndex == N:
                continue
            addValue = A[lastIndex]
            if addValue in dic:
                dic[addValue] += 1
            else:
                dic[addValue] = 1
            heappush(maxHeap, -addValue)
            heappush(minHeap, addValue)
            continue

        # print("aaaaaa", lastIndex, firstIndex)
        answer += (lastIndex - firstIndex)

        if answer >= MAX_VALUE:
            return MAX_VALUE

        # 차이가 K보다 클 경우
        findNewStart()

    return answer + 1
