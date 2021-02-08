from sys import stdin

std = stdin.readline

N = int(std())
rope = []
for i in range(N):
    rope.append(int(std()))
rope.sort(reverse=True)

answer = 1
weight = rope[0]
for i in range(1, N):
    if rope[i] * (i+1) < weight and rope[i] * (answer+1) < weight:
        continue
    answer = i+1
    weight = (rope[i] * (answer))

print(weight)
