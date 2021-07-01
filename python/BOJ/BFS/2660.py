from sys import stdin

std = stdin.readline

N = int(std())

friend = [[]for i in range(N)]

while True:
    a, b = map(int, std().split())
    if a == -1 and b == -1:
        break
    friend[a-1].append(b-1)
    friend[b-1].append(a-1)

q = []


def bfs():
    check = [0 for i in range(N)]
    check[q[0][0]] = 1
    while q:
        a, d = q.pop(0)
        for f in friend[a]:
            if check[f] == 0:
                check[f] = d+1
                q.append((f, d+1))

    return max(check)


dic = {}

for i in range(N):
    q.append((i, 0))
    relation = bfs()
    if relation in dic:
        dic[relation].append(i)
    else:
        dic[relation] = [i]

min_dic = 50
for key in dic:
    if key < min_dic:
        min_dic = key

print(min_dic, len(dic[min_dic]))
for i in range(len(dic[min_dic])):
    print(dic[min_dic][i]+1, end=" ")
