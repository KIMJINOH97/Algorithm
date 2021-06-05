def solution(n):

    ans = 0

    i = 1
    while True:
        k = i*i
        if n == k:
            ans = i
            break
        elif k > n:
            return -1

        i += 1

    ans = n + ans * 2 + 1

    return ans
