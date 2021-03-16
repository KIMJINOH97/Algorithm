from sys import stdin

std = stdin.readline

arr, com = [], []
check = []


def combi(start):
    if len(com) == 6:
        print(*com)
        return
    for i in range(start, len(arr)):
        if check[i] == 0:
            check[i] = 1
            com.append(arr[i])
            combi(i)
            com.pop()
            check[i] = 0


while True:
    arr = list(map(int, std().split()))

    if arr[0] == 0:
        break
    n = arr[0]
    arr = arr[1:]
    check = [0 for i in range(n)]
    combi(0)
    print()
