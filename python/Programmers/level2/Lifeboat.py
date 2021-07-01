def solution(people, limit):
    answer = 0
    last = len(people)-1
    boat = []
    people.sort()
    j=0
    for i in range(last, -1, -1):
        if i<= j: break
        if people[i] + people[j] <= limit:
            answer+=1
            j +=1
            continue
        else:
            answer += 1
    if i==j: answer+=1
    return answer