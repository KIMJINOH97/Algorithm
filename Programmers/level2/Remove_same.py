def solution(s):
    answer = 0
    li = []
    for i in range(len(s)):
        li.append(s[i])
        if len(li) <= 1:
            continue   
        while True:
            if len(li) <= 1 or li[-1] != li[-2]:
                break
            if li[-1] == li[-2]:
                li.pop()
                li.pop()
    if len(li) == 0: answer = 1
    return answer