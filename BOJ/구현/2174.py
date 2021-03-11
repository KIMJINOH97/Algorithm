from sys import stdin

std = stdin.readline

C, R = map(int, std().split())
N, M = map(int, std().split())

robot = [[0, 0] for i in range(N+1)]
board = [[[0, 0] for i in range(C)]for i in range(R)]

robot_num = 1
dic = {'E': 0, 'S': 1, 'W': 2, 'N': 3}
for i in range(N):
    x, y, direction = std().split()
    x, y = int(x)-1, R-int(y)
    board[y][x][0] = robot_num
    board[y][x][1] = dic[direction]
    robot[robot_num] = [y, x]
    robot_num += 1

nr, nc = [0, 1, 0, -1], [1, 0, -1, 0]

ok = True
for i in range(M):
    r_num, what, count = std().split()
    r_num, count = int(r_num), int(count)

    row, column = robot[r_num][0], robot[r_num][1]
    direct = board[row][column][1]
    ok = True
    if what == 'F':
        for i in range(count):
            dr, dc = row+nr[direct]*(i+1), column+nc[direct]*(i+1)
            if 0 <= dr < R and 0 <= dc < C:
                if board[dr][dc][0] != 0:
                    print('Robot %d crashes into robot %d' %
                          (r_num, board[dr][dc][0]))
                    ok = False
                    break
            else:
                print('Robot %d crashes into the wall' % r_num)
                ok = False
                break
        if ok:
            new_row, new_column = row+nr[direct]*count, column+nc[direct]*count
            board[row][column] = [0, 0]
            robot[r_num] = [new_row, new_column]
            board[new_row][new_column] = [r_num, direct]
    elif what == 'L':
        board[row][column][1] = (direct-count) % 4
    elif what == 'R':
        board[row][column][1] = (direct+count) % 4

    if ok == False:
        break

if ok:
    print("OK")
