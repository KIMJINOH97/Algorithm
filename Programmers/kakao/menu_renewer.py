def solution(orders, course):
    answer = []
    order_len = [len(m) for m in orders]
    order_max = max(order_len)
    dic = {}
    check = [0 for i in range(10)]
    for i, order in enumerate(orders):
        orders[i] = sorted(order)

    def combi(n, ans, start, row):
        if len(ans) == n:
            if ans not in dic:
                dic[ans] = 1
            else:
                dic[ans] += 1
            return 0
        for i in range(start, len(orders[row])):
            if check[i] == 0:
                check[i] = 1
                combi(n, ans+orders[row][i], i+1, row)
                check[i] = 0

    for c in course:
        for j in range(len(orders)):
            if c <= order_max:
                combi(c, "", 0, j)
    c_max = []
    for c in course:
        count_max = 0
        for key in dic:
            if len(key) == c and dic[key] > count_max:
                count_max = dic[key]
        c_max.append(count_max)

    for i, count in enumerate(c_max):
        for key in dic:
            if dic[key] == count and count >= 2 and len(key) == course[i]:
                answer.append(key)
    answer.sort()

    return answer
