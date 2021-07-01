def solution(lottos, win_nums):
    answer = []
    dic = {}
    high, low = 0, 0
    for win in win_nums:
        if win not in dic:
            dic[win] = 1

    for l in lottos:
        if l == 0:
            high += 1
        elif l in dic:
            high += 1
            low += 1

    score = {6: 1, 5: 2, 4: 3, 3: 4, 2: 5, 1: 6, 0: 6}
    answer = [score[high], score[low]]
    return answer
