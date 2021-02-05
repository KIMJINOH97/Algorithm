from sys import stdin

N = int(stdin.readline())
li = list(map(int, stdin.readline().split()))
li = sorted(li)
S = int(stdin.readline())

first, last = 0, len(li)-1
answer = 0

while first < last:
    ob = li[first] + li[last]
    if ob == S:
        answer += 1
        first += 1
    elif ob < S:
        first += 1
    else:
        last -= 1

print(answer)
