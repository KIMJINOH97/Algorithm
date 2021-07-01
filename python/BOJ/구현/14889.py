from sys import stdin
from copy import deepcopy

std = stdin.readline
N = int(std())
team = []
for i in range(N):
    team.append(list(map(int, std().split())))

start_team = []
t = []
check = [0 for i in range(N)]


def combi(n, start):
    if len(t) == n:
        start_team.append(list(t))
        return

    for i in range(start, N):
        if check[i] == 0:
            check[i] = 1
            t.append(i)
            combi(n, i+1)
            t.pop()
            check[i] = 0


combi(N//2, 0)
answer = 40000

for st in start_team:
    start_sum = 0
    link_team = []
    for i in range(N):
        if i not in st:
            link_team.append(i)
    for i in range(N//2):
        for j in range(i+1, N//2):
            start_sum += team[st[i]][st[j]]
            start_sum += team[st[j]][st[i]]
    link_sum = 0

    for i in range(N//2):
        for j in range(i+1, N//2):
            link_sum += team[link_team[i]][link_team[j]]
            link_sum += team[link_team[j]][link_team[i]]

    minus = abs(start_sum - link_sum)
    if minus < answer:
        answer = minus

print(answer)
