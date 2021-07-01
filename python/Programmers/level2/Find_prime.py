import math

num_li = []
check = []

def dfs(numbers, s, index, length, c):
    if index == length:
        num_li.append(s)
        return
    for i, n in enumerate(numbers):
        if c[i] == 0:
            c[i] = 1
            y = s+n
            dfs(numbers, y, index, length+1, c)
            c[i] = 0
    
def prime(number):
    if number < 2: return 0
    for i in range(2, number):
        if number % i == 0:
            return 0
    return 1

def solution(numbers):
    answer = 0
    check = [0 for i in range(len(numbers))]
    for i in range(1, len(numbers)+1):#나올 수 있는 숫자 길이
        dfs(numbers, "", i, 0, check)
    #print(num_li)
    for i in range(len(num_li)): num_li[i] = int(num_li[i])
    number_li = list(set(num_li))
    for n in number_li:
        print(n)
        if prime(n) == 1:
            answer += 1
    
    return answer