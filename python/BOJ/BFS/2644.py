from sys import stdin

std = stdin.readline
N = int(std())

chon = [[] for i in range(N+1)]
a, b = map(int, std().split())
n = int(std())
for i in range(n):
    parent, son = map(int, std().split())
    chon[parent].append(son)
    chon[son].append(parent)

q = []
check = [-1 for i in range(N+1)]
q.append((a, 1))
while q:
    p, num = q.pop(0)
    for child in chon[p]:
        if check[child] == -1:
            check[child] = num
            q.append((child, num+1))

print(check[b])
