from sys import stdin

std = stdin.readline

F, S, G, U, D = map(int, std().split())

elevator = [0 for i in range(F+1)]
check = [0 for i in range(F+1)]
q = [(S, 0)]
check[S] = 1
while q:
    floor, d = q.pop(0)
    if floor + U <= F and check[floor+U] == 0:
        check[floor+U] = 1
        elevator[floor+U] = d+1
        q.append((floor+U, d+1))
    if floor - D >= 1 and check[floor-D] == 0:
        check[floor-D] = 1
        elevator[floor-D] = d+1
        q.append((floor-D, d+1))

print("use the stairs" if elevator[G] == 0 and check[G] == 0 else elevator[G])
