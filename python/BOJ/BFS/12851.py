from sys import stdin

std = stdin.readline

N, K = map(int, std().split())

hide = [-1 for i in range(100001)]
hide[N] = 0

q = [(N, 0)]

ans = 0
while q:
    ver, d = q.pop(0)
    if hide[K] > 0 and ver == K and d == hide[K]:
        ans += 1
        continue

    if hide[K] >= 0 and d > hide[K]:
        break

    if ver - 1 >= 0 and (hide[ver-1] < 0 or hide[ver-1] == d+1):
        hide[ver-1] = d+1
        q.append((ver-1, d+1))
    if ver + 1 <= 100000 and (hide[ver+1] < 0 or hide[ver+1] == d+1):
        hide[ver+1] = d+1
        q.append((ver+1, d+1))
    if ver * 2 <= 100000 and (hide[ver*2] < 0 or hide[ver*2] == d+1):
        hide[ver*2] = d+1
        q.append((ver*2, d+1))
if N == K:
    print("0")
    print("1")
else:
    print(hide[K])
    print(ans)
