from sys import stdin

std = stdin.readline

N = int(std())
num = []
for i in range(N):
    a = int(std())
    num.append((a, abs(a)))

num = sorted(num, key=lambda x: -x[1])
answer = 0

while num:
    ans = num[0][0]
    index = -1
    for i in range(1, len(num)):
        if ans > 0:
            if num[i][0] > 1:
                index = i
                ans *= num[i][0]
                break
        else:
            if num[i][0] <= 0:
                index = i
                ans *= num[i][0]
                break
    answer += ans
    if not index == -1:
        num.pop(index)
    num.pop(0)

print(answer)
