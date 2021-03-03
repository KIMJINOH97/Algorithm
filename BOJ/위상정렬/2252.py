from sys import stdin

std = stdin.readline

T = int(std())

while T > 0:
    T -= 1
    N = int(std())

    edge = [[0 for i in range(N)]for i in range(N)]
    score = list(map(lambda x: int(x)-1, std().split()))
    degree = [0 for i in range(N)]

    for i in range(N):
        for j in range(i+1, N):
            a, b = score[i], score[j]
            edge[a][b] = 1
            degree[b] += 1

    m = int(std())  # 팀 등수가 바뀐 것들 a<b -> a>b
    flag = True
    for i in range(m):
        v1, v2 = map(int, std().split())
        v1, v2 = v1-1, v2-1  # 팀들
        a, b = score.index(v1), score.index(v2)  # 팀들의 등수
        if a < b:  # 원래 a 등수가 더 높았음
            edge[v1][v2] = 0
            degree[v2] -= 1
            edge[v2][v1] = 1
            degree[v1] += 1
        else:
            edge[v2][v1] = 0
            degree[v1] -= 1
            edge[v1][v2] = 1
            degree[v2] += 1

    q, answer = [], []

    for i in range(N):
        if degree[i] == 0:
            q.append((i, 1))
    flag = False

    if len(q) == 0:
        answer = "IMPOSSIBLE"
        flag = True
    elif len(q) >= 2:
        answer = "?"
        flag = True
    else:
        while q:
            vertax, d = q.pop(0)
            answer.append(vertax+1)
            cnt = 0
            for i in range(N):
                if edge[vertax][i] == 1:
                    degree[i] -= 1
                    if degree[i] == 0:
                        cnt += 1
                        q.append((i, d+1))
            if cnt >= 2:
                flag = True
                answer = "?"
                break
            if d < N and cnt == 0:
                flag = True
                answer = "IMPOSSIBLE"
                break

    if flag:
        print(answer)
    else:
        if min(answer) == 0:
            print("IMPOSSIBLE")
        else:
            for a in answer:
                print(a, end=" ")
            print()
