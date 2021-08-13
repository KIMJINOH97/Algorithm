from heapq import heappop, heappush


def solution(n, start, a, b, fares):
    INF = 1000000000
    edge = [[] for i in range(n)]

    start, a, b = start-1, a-1, b-1
    for fare in fares:
        s, e, d = fare
        s, e = s-1, e-1
        edge[s].append((e, d))
        edge[e].append((s, d))
    q = []

    def dijkstra(k):
        dist = [INF for i in range(n)]
        dist[k] = 0
        q.append((0, k))
        while q:
            d, vertax = heappop(q)

            if d > dist[vertax]:
                continue

            for ver in edge[vertax]:
                end, distance = ver
                if distance + d < dist[end]:
                    dist[end] = distance + d
                    heappush(q, (dist[end], end))

        return dist

    d = dijkstra(start)
    answer = INF
    for i in range(n):
        dis = dijkstra(i)
        # d[i] 공통으로 타고 간 거리
        answer = min(answer, d[i] + dis[a] + dis[b])

    return answer
