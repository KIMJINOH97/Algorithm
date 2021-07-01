from sys import stdin

std = stdin.readline

T = int(std())
two = []

for i in range(T):
    two.append(list(map(int, std().split())))

q, prime = [], [1 for i in range(10000)]


def bfs(end):
    check = [-1 for i in range(10000)]
    check[q[0][0]] = 0
    while q:
        n, d = q.pop(0)
        if check[end] != -1:
            break
        n = str(n)
        for i in range(4):
            for j in range(10):
                if i == 0 and j == 0:
                    continue
                a = n[0:i] + str(j) + n[i+1:]
                a = int(a)
                if prime[a] == 1 and check[a] == -1:
                    check[a] = d+1
                    q.append((a, d+1))
    return check[end]


for i in range(2, 5000):
    for j in range(i+i, 10000, i):
        if prime[j] == 1:
            prime[j] = 0

for t in two:
    start, end = t
    q.append((start, 0))
    answer = bfs(end)
    print(answer if answer >= 0 else "Impossible")
    q = []
