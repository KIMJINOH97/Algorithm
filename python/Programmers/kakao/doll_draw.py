def solution(board, moves):
    answer = 0
    n = len(board)
    stack = []

    def find(col):
        for i in range(n):
            up = board[i][col]
            if up != 0:
                board[i][col] = 0
                return up
        return -1

    for move in moves:
        m = find(move-1)
        if m == -1:
            continue
        if len(stack) == 0:
            stack.append(m)
        else:
            last = stack[-1]
            if last == m:
                stack.pop()
                answer += 2
            else:
                stack.append(m)

    return answer
