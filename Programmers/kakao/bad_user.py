from itertools import permutations, combinations


def solution(user_id, banned_id):
    answer = 0
    B = len(banned_id)
    com_list = list(combinations(user_id, B))

    def is_match(user, ban):
        if len(user) != len(ban):
            return False
        for u, b in zip(user, ban):
            if b == "*":
                continue
            elif u == b:
                continue
            else:
                return False
        return True

    for com in com_list:
        per = list(permutations(com, B))
        for p in per:
            is_ban = True
            for i in range(B):
                if not is_match(p[i], banned_id[i]):
                    is_ban = False
                    break

            if is_ban:
                answer += 1
                break

    return answer
