from sys import stdin

std = stdin.readline

R, C, B = map(int, std().split())

height = [0 for i in range(257)]

for i in range(R):
    a = list(map(int, std().split()))
    for j in range(C):
        height[a[j]] += 1

time, b = 1000000000, 0
for k in range(257):
    up, down = 0, 0
    for h in range(257):
        if h < k:
            up += height[h]*(k-h)
        else:
            down += height[h]*(h-k)
    if up > down+B:
        continue
    t = up + 2*down
    if t <= time:
        time = t
        b = k

print(time, b)
