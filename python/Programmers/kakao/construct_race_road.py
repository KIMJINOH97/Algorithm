from collections import deque

def solution(board):
    GARO, SERO, WALL = 0, 1, 1
    N = len(board)
    
    q = deque()
    
    nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
    
    dist = [[100000000 for i in range(N)] for j in range(N)]
    dist[0][0] = 0
    if board[0][1] == 0:
        dist[0][1] = 100
        q.append((100, 0, 1, GARO))
    if board[1][0] == 0:
        dist[1][0] = 100
        q.append((100, 1, 0, SERO))
    
    while q:
        cost, r, c, where = q.popleft()
        
        for i in range(4):
            dr, dc = r + nr[i], c + nc[i]
            
            if dr < 0 or dc < 0 or dr >= N or dc >= N or board[dr][dc] == WALL:
                continue
                
            if cost > dist[dr][dc] + 600:
                continue
                
            if i % 2 == 0: # 가로방향
                if where == GARO:
                    dist[dr][dc] = min(dist[dr][dc], cost + 100)
                    q.append((cost+100, dr, dc, GARO))
                else:
                    dist[dr][dc] = min(dist[dr][dc], cost + 600)
                    q.append((cost+600, dr, dc, GARO))
            else:
                if where == SERO:
                    dist[dr][dc] = min(dist[dr][dc], cost + 100)
                    q.append((cost+100, dr, dc, SERO))
                else:
                    dist[dr][dc] = min(dist[dr][dc], cost + 600)
                    q.append((cost+600, dr, dc, SERO))
    
    for i in range(N):
        print(dist[i])
    
    return dist[N-1][N-1]