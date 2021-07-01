from sys import stdin

N, M = map(int, stdin.readline().split())
tree = list(map(int, stdin.readline().split()))
l, r = 0, max(tree)
answer = 0
while l <= r:
    mid = (l+r) // 2
    ans = 0
    for t in tree:
        if t > mid:
            ans += t-mid
        if ans >= M:
            break
    if ans >= M:
        if mid > answer:
            answer = mid
        l = mid+1
    else:
        r = mid-1
print(answer)
