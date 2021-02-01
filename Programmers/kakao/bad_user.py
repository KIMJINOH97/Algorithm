from itertools import permutations


def solution(user_id, banned_id):
    global answer
    answer = 0
    check = [0 for i in range(len(user_id))]
    ban_check = {user: 0 for user in user_id}
    c = []

    def match(user, ban):
        if len(user) != len(ban):
            return False
        for i in range(len(ban)):
            if ban[i] == '*' or ban[i] == user[i]:
                continue
            else:
                return False
        return True

    def right(arr):
        for ban in banned_id:
            for a in arr:
                if ban_check[a] == 0 and match(a, ban):
                    ban_check[a] = 1
                    break
            else:
                return False
        return True

    def combi(n, start):
        global answer
        if len(c) == n:
            flag = False
            per = list(permutations(c, len(c)))
            for p in per:
                flag = right(p)
                for key in ban_check:
                    ban_check[key] = 0
                if flag:
                    break

            if flag:
                answer += 1
            return
        for i in range(start, len(user_id)):
            if check[i] == 0:
                check[i] = 1
                c.append(user_id[i])
                combi(n, i+1)
                check[i] = 0
                c.pop()

    combi(len(banned_id), 0)

    return answer
