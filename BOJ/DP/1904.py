from sys import stdin

N = int(stdin.readline())
a, b, c = 0, 0, 0
num = N
a, b = 1, 2

while num >= 3:
    num = num-1
    c = a + b
    b, a = c, b

if N == 1:
    print(a)
elif N == 2:
    print(b)
else:
    print(c % 15746)
