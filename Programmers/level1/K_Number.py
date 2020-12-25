def solution(array, commands):
    answer = []
    for com in commands:
        li = array[(com[0]-1):com[1]]
        li.sort()
        answer.append(li[com[2]-1])
        
    return answer