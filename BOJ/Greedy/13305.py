from sys import stdin

std = stdin.readline
N = int(std())

dist = list(map(int, std().split()))
oil = list(map(int, std().split()))

answer = 0

least_oil = oil[0]

for i, d in enumerate(dist):
    if oil[i] < least_oil:
        least_oil = oil[i]
    answer += d * least_oil

print(answer)
