def solution(tickets):
    answer = []
    tc = {}
    pro = []
    dic = {}
    for t in tickets:
        start, end = t[0], t[1]
        key = start+end
        if start in dic:
            dic[start].append(end)
        else:
            dic[start] = [end]
        if key in tc:
            tc[key] += 1
        else:
            tc[key] = 1
    check = {}

    def dfs(s, e):
        if len(answer) == len(tickets)+1:
            pro.append(list(answer))
            return

        if e in dic:
            for t in dic[e]:
                if check[e+t] != tc[e+t]:
                    check[e+t] += 1
                    answer.append(t)
                    dfs(e, t)
                    check[e+t] -= 1
                    answer.pop()
        return

    for t in dic['ICN']:
        check = {key: 0 for key in tc}
        answer = ['ICN', t]
        check['ICN'+t] = 1
        dfs('ICN', t)

    pro.sort()
    return pro[0]
