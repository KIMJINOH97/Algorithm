from sys import stdin

std = stdin.readline

A, B = map(int, std().split())


dic = {A: 0}

q = [(A, 0)]

while q:
    num, d = q.pop(0)
    twice = num*2
    add_one = int(str(num)+"1")
    if twice <= B and twice not in dic:
        dic[twice] = d+1
        q.append((twice, d+1))

    if add_one <= B and add_one not in dic:
        dic[add_one] = d+1
        q.append((add_one, d+1))

print("-1" if B not in dic else dic[B]+1)
