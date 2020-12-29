def solution(skill, skill_trees):
    answer = 0
    for sk in skill_trees:
        check = skill
        for i in range(len(sk)):
            index = check.find(sk[i])
            flag = True
            if index == -1:
                continue # 스킬에 정의되지 않은 것 or 이미 다 배운것
            if index == 0:
                check = check[1:] # 선행 스킬 remove
            else:
                flag = False
                break
        if flag == True:
            answer += 1
    return answer