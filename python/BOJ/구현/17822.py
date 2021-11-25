from sys import stdin
from collections import deque

std = stdin.readline

N, M, T = map(int, std().split())
CLOCK, UNCLOCK = 1, -1

circles = []
nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
q = deque()

for i in range(N):
    circles.append(list(map(int, std().split())))


def rotate(circle, direct, cnt):
    rotateCircle = [0 for i in range(M)]
    for i, c in enumerate(circle):
        index = (i + direct * cnt) % M
        rotateCircle[index] = c
    
    return rotateCircle


def checkAdj(check, j, k):
    check[j][k] == 1
    q.append((j, k))
    isSame = False
    while q:
        r, c = q.popleft()

        for i in range(4):
            dr, dc = r + nr[i], (c + nc[i]) % M

            if dr < 0 or dr >= N or check[dr][dc] != 0 or circles[j][k] != circles[dr][dc]:
                continue
            isSame = True
            check[dr][dc] = -1
            q.append((dr, dc))
    
    if isSame:
        check[j][k] = -1
    else:
        check[j][k] = 0
    

def calAvg():
    sumValue, cnt = 0, 0
    for i in range(N):
        for j in range(M):
            if circles[i][j] == -1:
                continue
            sumValue += circles[i][j]
            cnt += 1
    
    if cnt == 0:
        return

    avg = sumValue / cnt

    for i in range(N):
        for j in range(M):
            if circles[i][j] == -1:
                continue

            if avg < circles[i][j]:
                circles[i][j] -= 1
            elif avg > circles[i][j]:
                circles[i][j] += 1
            

for i in range(T):
    ci, di, ki = map(int, std().split())
    
    ix = 2
    circleIndex = ci - 1
    while circleIndex < N:
        if di == 0:
            circles[circleIndex] = rotate(circles[circleIndex], CLOCK, ki)
        else:
            circles[circleIndex] = rotate(circles[circleIndex], UNCLOCK, ki)

        circleIndex = ci * ix - 1
        ix += 1
        

    check = [[0 for i in range(M)] for j in range(N)]
    for j in range(N):
        for k in range(M):
            if check[j][k] == -1 or circles[j][k] == -1:
                continue

            checkAdj(check, j, k)

    isAdj = False
    for j in range(N):
        for k in range(M):
            if check[j][k] == -1:
                circles[j][k] = -1
                isAdj = True
    
    if isAdj == False:
        calAvg()
    
answer = 0

for i in range(N):
    for j in range(M):
        if circles[i][j] != -1:
            answer += circles[i][j]

print(answer)