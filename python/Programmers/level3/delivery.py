from heapq import heappop, heappush


def solution(N, road, K):
    answer = 0
    INF = 100000000
    dist = [[] for i in range(N)]
    for r in road:
        a, b, d = r
        dist[a-1].append((b-1, d))
        dist[b-1].append((a-1, d))

    def dijk(n):
        check = [INF for i in range(N)]
        check[n] = 0
        q = []
        heappush(q, (n, 0))
        while q:
            v, distance = heappop(q)
            if distance > check[v]:
                continue
            for vertax in dist[v]:
                next_vertax, d = vertax
                if check[next_vertax] > distance+d:
                    check[next_vertax] = distance+d
                    heappush(q, (next_vertax, distance+d))

        return check

    a = dijk(0)
    for d in a:
        if d <= K:
            answer += 1

    return answer
