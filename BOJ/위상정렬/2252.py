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
        for j in range(N):
            if score[j] > score[i]:  # 등수가 낮은 팀이 높은 팀을 가리킴
                edge[i][j] = 1
                degree[j] += 1

    m = int(std())  # 팀 등수가 바뀐 것들 a<b -> a>b
    flag = True
    for i in range(m):
        v1, v2 = map(int, std().split())
        v1, v2 = v1-1, v2-1
        a = score.index(v1)
        b = score.index(v2)
        if score[v1] < score[v2]:  # 원래 a 등수가 더 높았음
            edge[a][b] = 0
            degree[b] -= 1
            edge[b][a] = 1
            degree[a] += 1
        else:
            edge[b][a] = 0
            degree[a] -= 1
            edge[a][b] = 1
            degree[b] += 1

    q, answer = [], [0 for i in range(N)]

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
            answer[vertax] = d
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
