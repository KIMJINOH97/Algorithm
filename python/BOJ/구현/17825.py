from sys import stdin
from copy import deepcopy

global answer
std = stdin.readline
order = list(map(int, std().split()))

RED, BLUE = 0, 1
N, END = 4, 41
red_edge = [[] for i in range(41)]
blue_edge = [[] for i in range(41)]
blueHorse = [10, 20, 30]


def init():
    for i in range(0, 40, 2):
        red_edge[i].append(i + 2)
    red_edge[40].append(END)
    red_edge[10].append(13)
    red_edge[20].append(22)
    red_edge[30].append(28)
    # 왼쪽
    for i in range(13, 17, 3):
        blue_edge[i].append(i + 3)
    blue_edge[19].append(25)

    # 아래
    for i in range(20, 23, 2):
        blue_edge[i].append(i + 2)
    blue_edge[24].append(25)

    # 오른쪽
    blue_edge[28].append(27)
    blue_edge[27].append(26)
    blue_edge[26].append(25)

    # 위
    for i in range(25, 36, 5):
        blue_edge[i].append(i + 5)
    blue_edge[40].append(END)


answer = 0


def move(start, cnt, edgeInfo):
    edge = red_edge

    if edgeInfo == BLUE:
        edge = blue_edge
    elif start in blueHorse:
        cnt -= 1
        start = edge[start][1]
        edge = blue_edge
        edgeInfo = BLUE

    arrive = start

    for i in range(cnt):
        arrive = edge[arrive][0]
        if arrive == END:
            return END, RED

    if arrive == 40:
        return 40, RED
    return arrive, edgeInfo


def dfs(turn, horseCount, sumOfNum, horseDic):
    global answer
    if len(turn) == 0:
        if sumOfNum > answer:
            answer = sumOfNum
        return

    cnt = turn.pop(0)

    if horseCount > 0:  # 말이 더 남아 있을 때
        arrive, nextEdge = move(0, cnt, RED)
        if (arrive, nextEdge) not in horseDic:
            leftTurn = deepcopy(turn)
            dic = deepcopy(horseDic)
            dic[(arrive, RED)] = 1
            dfs(leftTurn, horseCount - 1, sumOfNum + arrive, dic)

    for key in horseDic:
        start, edgeInfo = key

        # 도착 지점
        arrive, nextEdge = move(start, cnt, edgeInfo)

        # 마지막 도착이거나 해당 칸에 말이 있을 때
        if (arrive, nextEdge) in horseDic:
            continue

        leftTurn = deepcopy(turn)
        dic = deepcopy(horseDic)

        dic.pop(key)
        if arrive != END:
            dic[(arrive, nextEdge)] = 1
        else:
            arrive = 0
        dfs(leftTurn, horseCount, sumOfNum + arrive, dic)


init()
dfs(order, N, 0, {})
print(answer)
