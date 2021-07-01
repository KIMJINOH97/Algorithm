from sys import stdin

std = stdin.readline

N = int(std())
n, c = [i for i in range(N+1)], [0 for i in range(N+1)]

for i in range(N):
    a = int(std())
    c[i+1] = a


def is_ok(node):
    s = []
    a, b = [], []
    check = [0 for i in range(N+1)]
    s.append(node)
    while s:
        no = s.pop()
        a.append(no)
        check[no] = 1
        if check[c[no]] == 0:
            check[c[no]] = 1
            s.append(c[no])
            b.append(c[no])
        else:
            b.append(c[no])
    return set(a) == set(a) & set(b)


answer = []
for i in range(N):
    if is_ok(i+1):
        answer.append(i + 1)
print(len(answer))
for a in answer:
    print(a)
