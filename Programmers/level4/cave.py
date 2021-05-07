from collections import deque


def solution(n, path, order):
    answer = True

    node = [[] for i in range(n)]
    degree = [0 for i in range(n)]
    for p in path:
        start, end = p
        node[start].append(end)
        node[end].append(start)

    priority = [[] for i in range(n)]
    for o in order:
        before, after = o
        priority[before].append(after)
        degree[after] += 1

    if degree[0] > 0:
        return False

    q = deque()
    check = [0 for i in range(n)]
    check[0] = 1
    q.append(0)

    while q:
        vertax = q.popleft()
        for ver in node[vertax]:
            if check[ver] == 0 and degree[ver] == 0:
                check[ver] = 1
                q.append(ver)

        for ver in priority[vertax]:
            degree[ver] -= 1
            if degree[ver] == 0:
                flag = False
                for v in node[ver]:
                    if check[v]:
                        flag = True
                        break
                if not flag:
                    continue
                check[ver] = 1
                q.append(ver)

    return False if min(check) == 0 else True
