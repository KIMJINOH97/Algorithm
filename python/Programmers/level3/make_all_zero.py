import sys

sys.setrecursionlimit(500001)


def solution(weights, infos):
    global answer
    answer = 0

    N = len(weights)
    edge = [[] for i in range(N)]

    sumOfweight, minWeight = 0, (10000000, -1)

    for i, weight in enumerate(weights):
        sumOfweight += weight
        if weight < minWeight[0]:
            minWeight = (weight, i)

    if sumOfweight != 0:
        return -1

    degree = [0 for i in range(N)]

    for info in infos:
        start, end = info
        edge[start].append(end)
        edge[end].append(start)

    def dfs(vertax, parent):
        global answer
        for ver in edge[vertax]:
            if ver == parent:
                continue
            dfs(ver, vertax)

        weight = weights[vertax]
        answer += abs(weight)
        if weight > 0:
            weights[parent] += weight
        else:
            weights[parent] += weight

    dfs(0, 0)

    return answer
