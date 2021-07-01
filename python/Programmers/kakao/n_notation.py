def solution(n, t, m, p):
    answer = ''
    dic = {10 : 'A', 11 : 'B', 12 : 'C' , 13: 'D', 14:'E', 15: 'F'}
    will = p+(t-1)*m # 미리 구해야할 스트링 길이
    str1, i = '0', 1
    while len(str1) < will:
        add = ''
        div = i
        while div > 0:
            remain = div % n
            if remain >= 10: add = dic[remain] + add
            else: add = str(remain) + add
            div = div // n
        str1 += add
        i+=1
    for i in range(t):
        answer += str1[p-1 + m*i]
    return answer