from sys import stdin

std = stdin.readline

N, D, K, COUPON_NUMBER = map(int, std().split())

bob = []
for i in range(N):
    bob.append(int(std()))

presentBob = []

global sumOfMenu, bobDic
bobDic = {key: 0 for key in range(D+1)}
sumOfMenu = 0

def pushBobDic(num):
    global sumOfMenu, bobDic
    if bobDic[num] == 0:
        sumOfMenu += 1
    bobDic[num] += 1
    
    return

def removeBobDic(num):
    global sumOfMenu, bobDic
    bobDic[num] -= 1
    if bobDic[num] == 0:
        sumOfMenu -= 1
    
    return

l, r = 0, K-1
    
for i in range(r+1):
    presentBob.append(bob[i])
    pushBobDic(bob[i])

answer = sumOfMenu

if COUPON_NUMBER not in bobDic:
    answer += 1

while True:
    removeBobDic(bob[l])
    l = (l+1) % N
    
    if l == 0:
        break
    
    r = (r+1) % N
    pushBobDic(bob[r])

    if bobDic[COUPON_NUMBER] > 0:
        answer = max(answer, sumOfMenu)
    else:
        answer = max(answer, sumOfMenu+1)

print(answer)