import math
def solution(n):
    contry = ['4','1','2']
    answer = ''
    div = 0
    while True:
        div = n%3
        n = n//3

        if div == 0:
            n -= 1
        if n < 0:
            break
        print(div)
        answer = contry[div] + answer
                       
    return answer