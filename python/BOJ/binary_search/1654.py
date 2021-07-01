from sys import stdin

K, N = map(int, stdin.readline().split())
row = []
for i in range(K):
    r = int(stdin.readline())
    row.append(r)

l, r = 0, 3000000000
answer = 0

while l <= r:
    mid = (l+r)//2
    ans = 0
    for ro in row:
        ans += ro // mid

    if ans >= N:
        answer = max(answer, mid)
        l = mid+1
    else:
        r = mid-1
print(answer)
