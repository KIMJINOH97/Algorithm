from sys import stdin

std = stdin.readline

N, S = map(int, std().split())

arr = list(map(int, std().split()))

s = 0
answer = 0


def bt(start, depth, n):
    global answer, s
    if depth == n:
        if s == S:
            answer += 1
        return

    for i in range(start, len(arr)):
        s += arr[i]
        bt(i+1, depth+1, n)
        s -= arr[i]


for i in range(1, N+1):
    bt(0, 0, i)
print(answer)
