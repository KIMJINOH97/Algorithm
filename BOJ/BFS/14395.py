from sys import stdin

std = stdin.readline
S, T = map(int, std().split())
t = {}
op = ['*', '-', '+', '/']
q = []
q.append((S, ''))
if S != T:
    while q:
        num, s = q.pop(0)
        for o in op:
            str1 = s + o
            if o == '*':
                k = num*num
            elif o == '-':
                k = num-num
            elif o == '+':
                k = num+num
            else:
                if not num == 0:
                    k = num // num
            if k <= T:
                if not k in t:
                    t[k] = str1
                    q.append((k, str1))
                elif len(t[k]) == len(str1):
                    if str1 < t[k]:
                        t[k] = str1
                if len(t[k]) > len(str1):
                    continue

    print("-1" if not T in t else t[T])
else:
    print("0")
