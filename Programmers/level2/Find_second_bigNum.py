def two(n):
    ans = 0
    while True:
        if n == 0: break
        if n % 2 == 0:
            n = n//2
            continue
        else:
            ans += 1
            n = n//2
    return ans

def solution(n):
    answer = 0
    num = two(n)
    n+=1
    while True:
        if num == two(n):
            return n
        else:
            n+=1
    return answer