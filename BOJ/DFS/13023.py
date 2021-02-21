from sys import stdin

std = stdin.readline

N, M = map(int, std().split())

friend = [[] for i in range(N)]

for i in range(M):
    a, b = map(int, std().split())
    friend[a].append(b)
    friend[b].append(a)

answer = []
ans = False

check = [0 for i in range(N)]


def dfs(b):
    global ans
    if len(answer) == 5:
        ans = True
        return

    for fr in friend[b]:
        if check[fr] == 0 and ans == False:
            check[fr] = 1
            answer.append(fr)
            dfs(fr)
            check[fr] = 0
            answer.pop()


for i in range(N):
    if ans == True:
        break
    answer = [i]
    check = [0 for i in range(N)]
    check[i] = 1
    dfs(i)

print("1" if ans else "0")
