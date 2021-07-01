def solution(r, c, board):
    answer = 0
    board = [list(b) for b in board]
    check = [[0 for i in range(c)] for j in range(r)]

    def find_same():
        for i in range(r-1):
            for j in range(c-1):
                k = board[i][j]
                if k == '':
                    continue
                if [board[i+1][j], board[i][j+1], board[i+1][j+1]] == [k, k, k]:
                    check[i][j], check[i+1][j], check[i][j +
                                                         1], check[i+1][j+1] = 1, 1, 1, 1

    def check_block():
        cnt = 0
        for i in range(r):
            for j in range(c):
                if check[i][j] == 1:
                    cnt += 1
                    board[i][j] = ''
                    check[i][j] = 0
        return cnt

    def down():
        column = []
        for i in range(c):
            cnt, co = 0, []
            for j in range(r):
                if board[j][i] != '':
                    co.append(board[j][i])
                    cnt += 1
            column.append(['']*(r-cnt) + co)

        for i in range(c):
            for j in range(r):
                board[j][i] = column[i][j]

    while True:
        find_same()
        count = check_block()
        if count == 0:
            break
        answer += count
        down()

    return answer


# 과거의 나
def solution(m, n, board):
    answer = 0
    check = [[0 for i in range(n)] for j in range(m)]
    n_board = [[board[j][i] for i in range(n)] for j in range(m)]

    # R M A F N T J C
    def check_same():
        for i in range(m-1):
            for j in range(n-1):
                same = n_board[i][j]
                a, b, c = n_board[i+1][j], n_board[i][j+1], n_board[i+1][j+1]
                if same == '':
                    continue
                if a == same and b == same and c == same:
                    check[i][j], check[i+1][j], check[i][j +
                                                         1], check[i+1][j+1] = 1, 1, 1, 1

    def count_same():
        cnt = 0
        for i in range(m):
            for j in range(n):
                if check[i][j] == 1:
                    n_board[i][j] = ''
                    cnt += 1
        return cnt

    def down():
        column = [[] for i in range(n)]
        for i in range(n):
            for j in range(m):
                if n_board[j][i] != '':
                    column[i].append(n_board[j][i])
                    n_board[j][i] = ''
        for i in range(n):
            length = len(column[i])
            for j in range(length):
                base = m-length
                n_board[base+j][i] = column[i][j]

    while True:
        check = [[0 for i in range(n)] for j in range(m)]
        check_same()
        plus = count_same()
        if count_same() == 0:
            break
        answer += plus
        down()

    return answer
