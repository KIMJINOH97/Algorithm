def solution(grid):
    answer = []
    ROW, COL = len(grid), len(grid[0])
    shootLaser = [[[0 for i in range(4)] for j in range(COL)] for k in range(ROW)]
    
    nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]
    
    def findNextDist(r, c, dist):
        if grid[r][c] == 'S':
            return dist
        
        if grid[r][c] == 'L':
            return (dist - 1) % 4
        
        if grid[r][c] == 'R':
            return (dist + 1) % 4
    
    def go(r, c, dist):
        p_row, p_col, p_dist = r, c, dist
        cnt = 1
        while True:
            p_row, p_col = (p_row + nr[p_dist]) % ROW, (p_col + nc[p_dist]) % COL
            p_dist = findNextDist(p_row, p_col, p_dist)
            
            if shootLaser[p_row][p_col][p_dist]:
                break
            shootLaser[p_row][p_col][p_dist] = 1
            cnt += 1
        
        return cnt
    
    for i in range(ROW):
        for j in range(COL):
            for k in range(4):
                if shootLaser[i][j][k]:
                    continue
                shootLaser[i][j][k] = 1
                answer.append(go(i, j, k))
    
    return sorted(answer)