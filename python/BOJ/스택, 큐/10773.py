from sys import stdin

N = int(stdin.readline())
s = []
s_sum = 0
for i in range(N):
    a = int(stdin.readline())
    if a == 0:
        k = s.pop()
        s_sum -= k
    else:
        s.append(a)
        s_sum += a

print(s_sum)
