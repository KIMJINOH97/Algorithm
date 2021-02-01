from heapq import heappush, heappop

INF = 99999999


def solution(n, s, a, b, fares):
    answer = INF
    s, a, b = s-1, a-1, b-1
    dist = [INF for i in range(n)]
    road = [[] for i in range(n)]
    hq = []
    for fare in fares:
        road[fare[0]-1].append((fare[1]-1, fare[2]))  # 지점, 거리
        road[fare[1]-1].append((fare[0]-1, fare[2]))

    def dijk(start, distance):
        heappush(hq, (start, 0))
        while hq:
            v, dis = heappop(hq)
            if dis > distance[v]:
                continue
            for i in range(len(road[v])):
                new_road = road[v][i][1] + dis
                if new_road < distance[road[v][i][0]]:
                    distance[road[v][i][0]] = new_road
                    heappush(hq, (road[v][i][0], new_road))
    dist[s] = 0
    dijk(s, dist)
    for i in range(n):
        d = [INF for i in range(n)]
        ans = 0
        dijk(i, d)
        if i == a:
            ans = dist[i] + d[b]
        elif i == b:
            ans = dist[i] + d[a]
        else:
            ans = dist[i] + d[a] + d[b]
        answer = min(ans, answer)
    return answer
