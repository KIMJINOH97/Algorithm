def solution(n):
    answer = 2
    pre = 1
    prepre = 1
    for i in range(2, n+1):
        answer = pre + prepre
        prepre = pre
        pre = answer

    return answer % 1000000007
