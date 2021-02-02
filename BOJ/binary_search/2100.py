from sys import stdin

N, C = map(int, stdin.readline().split())

wifi = []
for i in range(N):
    wifi.append(int(stdin.readline()))

wifi.sort()
answer = 0
l, r = 0, 1000000000

while l <= r:
    mid = (l+r) // 2
    ans = 1
    pre = wifi[0]
    for i in range(1, len(wifi)):
        if wifi[i] - pre >= mid:
            ans += 1
            pre = wifi[i]
    if ans >= C:
        if answer < mid:
            answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)
