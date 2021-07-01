from sys import stdin
from copy import deepcopy

std = stdin.readline
N, M, oil = map(int, std().split())
dist = []
for i in range(N):
    dist.append(list(map(int, std().split())))

dr_row, dr_col = map(lambda x: int(x)-1, std().split())
check_client = [0 for i in range(M)]

client = []
for i in range(M):
    client.append(list(map(lambda x: int(x)-1, std().split())))
client = sorted(client, key=lambda x: (x[0], x[1]))

q = []
nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
check = [[-1 for i in range(N)] for j in range(N)]


def bfs():
    while q:
        r, c, d = q.pop(0)
        for i in range(4):
            dr, dc = r+nr[i], c+nc[i]
            if 0 <= dr < N and 0 <= dc < N:
                if check[dr][dc] == -1 and dist[dr][dc] == 0:
                    check[dr][dc] = d+1
                    q.append((dr, dc, d+1))
    return


def min_client():
    global dr_row, dr_col
    m_client = [0, 0, 400]
    m_index = 0
    for i, cl in enumerate(client):
        r, c = cl[0], cl[1]
        if check[r][c] < m_client[2] and check_client[i] == 0:
            m_client = [r, c, check[r][c]]
            m_index = i
    check_client[m_index] = 1
    dr_row, dr_col = m_client[0], m_client[1]
    return m_client[2], m_index


answer = 0
for i in range(M):
    q.append((dr_row, dr_col, 0))
    check[dr_row][dr_col] = 0
    bfs()
    minus_oil, c_index = min_client()
    oil -= minus_oil
    if oil <= 0 or check[dr_row][dr_col] == -1:
        answer = -1
        break
    check = [[-1 for i in range(N)] for j in range(N)]
    q.append((dr_row, dr_col, 0))
    check[dr_row][dr_col] = 1
    bfs()
    des_r, des_c = client[c_index][2], client[c_index][3]
    oil -= check[des_r][des_c]
    dr_row, dr_col = des_r, des_c
    if oil < 0 or check[des_r][des_c] == -1:
        answer = -1
        break
    oil += check[des_r][des_c]*2
    check = [[-1 for i in range(N)] for j in range(N)]
else:
    answer = oil
print(answer)
