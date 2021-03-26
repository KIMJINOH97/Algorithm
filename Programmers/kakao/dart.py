import re


def solution(dartResult):
    p = re.compile('[0-9]+|[SDT*#]')
    dart = p.findall(dartResult)
    answer = []

    for i, d in enumerate(dart):
        if d.isdigit():
            if i != 0:
                answer.append(num)
            num = int(d)
        else:
            if d == 'D':
                num = pow(num, 2)
            elif d == 'T':
                num = pow(num, 3)
            elif d == '*':
                num *= 2
                if len(answer) > 0:
                    answer[-1] *= 2
            elif d == '#':
                num *= -1

    return sum(answer)+num
