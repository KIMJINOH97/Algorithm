from sys import stdin
std = stdin.readline

N, S = map(int, std().split())
li = list(map(int, std().split()))
l, r = 0, 1

answer = 100001
sn = li[0]+li[1]
sn_len = 2
while l <= r:
    if sn >= S:
        if answer > sn_len:
            answer = sn_len
        sn_len -= 1
        sn -= li[l]
        l += 1
    else:
        sn_len += 1
        r += 1
        if r == len(li):
            break
        sn += li[r]

if answer == 100001:
    print("0")
else:
    print(answer)
