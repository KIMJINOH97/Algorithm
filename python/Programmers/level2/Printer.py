def solution(priorities, location):
    answer = 0
    delay = []
    for i in range(len(priorities)):
        delay.append(i)
    while True:
        flag = False
        for pr in priorities:
            if priorities[delay[0]] < pr:
                flag = True
                delay.append(delay[0])
                delay = delay[1:]
                break
        if flag == False:
            answer += 1
            if location == delay[0]:
                break
            priorities[delay[0]]=-1
            delay = delay[1:]
    return answer