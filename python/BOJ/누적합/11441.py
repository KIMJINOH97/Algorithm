from sys import stdin

std = stdin.readline
N = int(std())

li = list(map(int, std().split()))

stackSum = []

sumOfli = 0
for num in li:
    sumOfli += num
    stackSum.append(sumOfli)

M = int(std())
for i in range(M):
    start, end = map(lambda x: int(x) - 1, std().split())
    print(stackSum[end] - stackSum[start-1]
          if start-1 >= 0 else stackSum[end])
