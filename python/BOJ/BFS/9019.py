from sys import stdin

std = stdin.readline

N = int(std())

q = []


def dslr(ans):
    check = [0 for i in range(10000)]
    check[q[0]] = ''
    while q:
        if check[ans] != 0:
            return check[ans]
        a = q.pop(0)
        op = check[a]
        D = 2*a % 10000
        S = (a - 1) % 10000

        if check[D] == 0:
            check[D] = op+'D'
            q.append(D)
        if check[S] == 0:
            check[S] = op+'S'
            q.append(S)

        new_a = ''
        for i in range(4 - len(str(a))):
            new_a += '0'
        new_a += str(a)
        L = new_a[1]+new_a[2]+new_a[3]+new_a[0]
        R = new_a[3]+new_a[0]+new_a[1]+new_a[2]
        int_L, int_R = int(L), int(R)
        if check[int_L] == 0:
            check[int_L] = op+'L'
            q.append(int_L)
        if check[int_R] == 0:
            check[int_R] = op+'R'
            q.append(int_R)


answer = []

for i in range(N):
    x, y = map(int, std().split())
    q.append(x)
    answer.append(dslr(y))
    q = []

for a in answer:
    print(a)
