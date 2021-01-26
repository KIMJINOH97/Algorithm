import re


def solution(expression):
    answer = 0
    operation = ['*', '+', '-']
    check = [0 for i in range(len(operation))]
    op = []

    def fact(n, result, count):
        if count == n:
            op.append(result)
            return
        for i in range(3):
            if check[i] == 0:
                check[i] = 1
                fact(n, result+operation[i], count+1)
                check[i] = 0

    fact(3, "", 0)
    ex = re.findall('[0-9]+|[\+\*\-]', expression)
    for i, e in enumerate(ex):  # 수는 int형으로 변환
        if e not in operation:
            ex[i] = int(e)

    for o in op:
        li = ex
        for s in o:
            arr = []
            i = 0
            while i < len(li):
                if type(li[i]) is int or s != li[i]:
                    arr.append(li[i])
                    i += 1
                    continue
                if s == '*' and li[i] == '*':
                    arr[-1] *= li[i+1]
                elif s == '+' and li[i] == '+':
                    arr[-1] += li[i+1]
                elif s == '-' and li[i] == '-':
                    arr[-1] -= li[i+1]
                i += 2
            li = arr
        if abs(li[0]) > answer:
            answer = abs(li[0])
    return answer
