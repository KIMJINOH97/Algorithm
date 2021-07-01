from sys import stdin

std = stdin.readline
N, M = map(int, std().split())
island = [[]for i in range(N)]

for i in range(M):
    a, b, d = map(int, std().split())
    island[a-1].append((b-1, d))
    island[b-1].append((a-1, d))

start, end = map(int, std().split())
start, end = start-1, end-1


def bfs(d):
    q = []
    check = [0 for i in range(N)]
    q.append(start)
    check[start] = 1
    while q:
        ver = q.pop(0)
        for v in island[ver]:
            go, distance = v
            if distance >= d and check[go] == 0:
                q.append(go)
                check[go] = 1
    if check[end] == 1:
        return True
    return False


l, r = 0, 1000000000
answer = 0
while l <= r:
    mid = (l+r)//2
    result = bfs(mid)
    if not result:
        r = mid-1
    else:
        if mid > answer:
            answer = mid
        l = mid+1

print(answer)
