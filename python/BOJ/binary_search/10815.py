from sys import stdin

std = stdin.readline

N = int(std())

card = list(map(int, std().split()))
card.sort()
M = int(std())
find = list(map(int, std().split()))

answer = []


def bs(k):
    l, r = 0, len(card)-1
    while l <= r:
        mid = (l+r)//2

        if k <= card[mid]:
            if k == card[mid]:
                return 1
            r = mid-1
        else:
            l = mid+1
    return 0


for f in find:
    answer.append(bs(f))

print(*answer)
