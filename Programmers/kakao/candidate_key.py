from itertools import combinations


def solution(relation):
    answer = []
    l_tuple, l_relation = len(relation[0]), len(relation)
    key = [i for i in range(l_tuple)]
    all_keys = []
    for i in range(1, l_tuple+1):
        all_keys.append(list(combinations(key, i)))

    for keys in all_keys:
        for key in keys:
            same = 0
            # 부분 집합 판별
            s_key = set(key)
            for a in answer:
                s_a = set(a)
                if s_key & s_a == s_a:
                    same = 1
                    break
            if same:
                continue

            cmp = ["" for i in range(l_relation)]
            for k in key:
                for j in range(l_relation):
                    cmp[j] += relation[j][k]

            if len(set(cmp)) == l_relation:
                answer.append(key)

    return len(answer)
