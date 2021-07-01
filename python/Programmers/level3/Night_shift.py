import heapq


def solution(n, works):
    answer = 0
    h = []
    for w in works:
        heapq.heappush(h, -w)
    for i in range(n):
        work_max = heapq.heappop(h)
        work_max += 1
        heapq.heappush(h, work_max)
    for w in h:
        if w <= 0:
            answer += w*w
    return answer
