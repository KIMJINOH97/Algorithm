def solution(gems):
    answer = []
    gem = set(gems)
    gem_cnt = len(gem)
    check = {g: 0 for g in gem}

    l, r = 0, 0
    cnt = 1
    check[gems[0]] = 1

    while l <= r:
        if cnt == gem_cnt:
            answer.append([l+1, r+1])
            if check[gems[l]] == 1:
                cnt -= 1
            check[gems[l]] -= 1
            l += 1
        elif cnt < gem_cnt:
            r += 1
            if r >= len(gems):
                break
            if check[gems[r]] == 0:
                cnt += 1
            check[gems[r]] += 1
    answer.sort(key=lambda x: (x[1]-x[0], x[0]))
    return answer[0]
