import re

def solution(s):
    p = re.compile('{[0-9,]+}')
    ans, answer = [], []
    s = s[1:-1]
    li = p.findall(s)
    
    for l in li:
        a = list(l[1:-1].split(','))
        ans.append(a)
    ans = sorted(ans, key = lambda x: len(x))
    answer.append(int(ans[0][0]))
    for i in range(len(ans)-1):
        A = list(set(ans[i+1]) - set(ans[i]))
        answer.append(int(A[0]))
        
    return answer