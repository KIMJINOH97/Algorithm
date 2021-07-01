def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1

    dic = {}
    foody = [(f, i) for i, f in enumerate(food_times)]
    foody = sorted(foody)

    for food in foody:
        time, index = food
        if time in dic:
            dic[time].append(index)
        if time not in dic:
            dic[time] = [index]

    food_cnt = len(food_times)
    time = 0

    for key in dic:
        eaten = len(dic[key])  # 다 먹은 음식 개수
        minus = (key-time)*food_cnt  # 남은 음식 개수 * 시간 만큼 걸림
        time = key
        if k-minus < 0:
            remain_index = k % food_cnt
            #print(k, food_cnt, remain_index)
            check_food = [0 for i in range(len(food_times))]

            # 다 먹은 음식 체크
            for t in dic:
                if t < key:
                    for j in range(len(dic[t])):
                        index = dic[t][j]
                        check_food[index] = 1

            # print(check_food)
            remain_food, cnt = [], 0
            for i, food in enumerate(food_times):
                if check_food[i] == 0:
                    remain_food.append(i)

            # print(remain_food)
            return remain_food[remain_index]+1

        k -= minus
        food_cnt -= eaten  # 다 먹은 음식 빼주기
        if food_cnt == 0:
            return -1

    return
