def solution(prices):
    answer = []
    p = []
    for i in range(len(prices)): answer.append(0)
    for i in range(len(prices)):
        if len(p) == 0:
            p.append([i, prices[i]])
            continue
        if p[-1][1] <= prices[i]:
            p.append([i, prices[i]])
        else:
            while True:
                if len(p) == 0 or p[-1][1] <= prices[i]:
                    p.append([i, prices[i]])
                    break
                if len(p) != 0 and p[-1][1] > prices[i]:
                    answer[p[-1][0]] = i-p[-1][0]
                    p.pop(-1)
                    
    while len(p) != 0:
        answer[p[-1][0]] = i - p[-1][0]
        p.pop(-1)
    return answer