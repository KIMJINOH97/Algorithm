from itertools import combinations


def solution(orders, course):
    answer = []
    order_list = []
    for order in orders:
        menu = list(order)
        for c in course:
            if c > len(order):
                continue
            for com in combinations(order, c):
                arr = ''.join(sorted(list(com)))
                order_list.append(arr)

    dic = {}
    order_len = [0 for i in range(11)]
    for order in order_list:
        if order not in dic:
            dic[order] = 1
        else:
            dic[order] += 1
        o_len = len(order)
        if dic[order] > order_len[o_len]:
            order_len[o_len] = dic[order]

    for key in dic:
        k_len = len(key)
        if order_len[k_len] > 1 and order_len[k_len] == dic[key]:
            answer.append(key)

    answer.sort()
    return answer
