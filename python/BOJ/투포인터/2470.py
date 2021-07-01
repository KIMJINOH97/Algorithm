from sys import stdin
std = stdin.readline

N = int(std())
li = list(map(int, std().split()))
li = sorted(li)
l, r = 0, N-1
answer = []
min_two = 2000000000
while l < r:
    two = li[l] + li[r]
    if abs(two) < abs(min_two):
        min_two = two
        answer = [li[l], li[r]]
    if two == 0:
        break
    elif two < 0:
        l += 1
    else:
        r -= 1


print(*answer)
