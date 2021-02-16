import re


def solution(dartResult):
    p = re.compile('[0-9]+|[#*SDT]')
    da = p.findall(dartResult)
    answer = 0
    pre = 0
    num = 0
    for dart in da:
        if dart.isdigit():
            pre = num
            answer += num
            num = int(dart)
        else:
            if dart == 'D':
                num = pow(num, 2)
            elif dart == 'T':
                num = pow(num, 3)
            elif dart == '#':
                num = -num
            elif dart == '*':
                answer -= pre
                answer += pre*2
                num *= 2

    return answer+num
