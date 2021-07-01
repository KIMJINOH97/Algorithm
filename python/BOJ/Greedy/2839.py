from sys import stdin

std = stdin.readline

N = int(std())

box = 0
ans = -1
for i in range(N//3+1):
    box = N - 3*i
    five = box // 5
    if box % 5 == 0:
        ans = i+five
        break

print(ans)
