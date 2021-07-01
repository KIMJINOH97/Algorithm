def find_m(n, c):
    answer = 0
    for c_num in c:
        if c_num >= n:
            answer+=1
    return answer
    
def find_n(n,c):
    answer=0
    for c_num in c:
        if c_num <= n:
            answer+=1
    return answer
    
def solution(c):
    answer = 0
    c.sort()
    for i in range(c[-1], 0, -1):
        more = find_m(i, c)
        nomore = find_n(i, c)
        if more >= i and nomore <= i:
            return i
            
    return answer