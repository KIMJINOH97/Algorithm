def solution(enroll, referral, seller, amount):
    answer = []
    amount = list(map(lambda x: x*100, amount))
    people = {}
    money = {"-": 0}
    for e, r in zip(enroll, referral):
        people[e] = r
        money[e] = 0

    def give(name, m):
        if name == "-":
            return
        money[name] += m
        go = int(m*0.1)

        if go == 0:
            return

        money[name] -= go

        next_p = people[name]
        give(next_p, go)

    for s, a in zip(seller, amount):
        give(s, a)

    for e in enroll:
        answer.append(money[e])

    return answer
