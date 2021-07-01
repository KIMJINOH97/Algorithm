from sys import stdin


std = stdin.readline

N, M = map(int, std().split())

D = list(map(int, std().split()))

P = []
ans = 0
for i in range(N):
    ans += D[i]
    P.append(ans)

answer = []
for i in range(M):
    a, b = map(int, std().split())
    answer.append(P[b-1]-P[a-1]+D[a-1])

for a in answer:
    print(a)
