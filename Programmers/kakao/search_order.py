from itertools import combinations
from copy import deepcopy


def solution(information, queries):
    answer = []
    information = list(map(lambda x: x.split(), information))

    pick = [0, 1, 2, 3]
    combi = []
    for i in range(1, 5):
        combi.append(list(combinations(pick, i)))

    dic = {}
    for info in information:
        score = int(info[-1])
        k = info[:-1]
        key = ''.join(k)
        if key in dic:
            dic[key].append(score)
        else:
            dic[key] = [score]
        for com in combi:
            for co in com:
                key = deepcopy(k)
                for c in co:
                    key[c] = '-'
                key = ''.join(key)
                if key in dic:
                    dic[key].append(score)
                else:
                    dic[key] = [score]

    for key in dic:
        dic[key].sort()

    for query in queries:
        q = list(filter(lambda x: x != 'and', query.split()))
        score = int(q.pop())
        key = ''.join(q)
        if not key in dic:
            answer.append(0)
            continue

        l, r, index = 0, len(dic[key])-1, len(dic[key])
        while l <= r:
            mid = (l+r) // 2
            if dic[key][mid] >= score:
                index = mid
                r = mid-1
            else:
                l = mid+1
        answer.append(len(dic[key]) - index)

    return answer
