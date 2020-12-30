import heapq

def solution(sco, K):
    answer = 0
    heapq.heapify(sco)
    while True:
        if sco[0] >= K:
            break
        if len(sco) <= 1:
            return -1
        else:
            first = heapq.heappop(sco)
            second = heapq.heappop(sco)
            mix = first + second*2
            answer+=1
            heapq.heappush(sco, mix)
    return answer