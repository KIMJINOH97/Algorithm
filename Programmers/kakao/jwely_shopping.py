def solution(gems):
    answer = []
    dia = set(gems)
    check = {j: 0 for j in dia}

    l, r = 0, 0
    check[gems[l]] += 1
    cnt = 1

    while l <= r:
        if r == len(gems)-1 and r-l+1 < len(dia):
            break
        if cnt == len(dia):
            answer.append([l+1, r+1])
            check[gems[l]] -= 1
            if check[gems[l]] == 0:
                cnt -= 1
            l += 1
        else:
            if r != len(gems) - 1:
                r += 1
                if check[gems[r]] == 0:
                    cnt += 1
                check[gems[r]] += 1
            else:
                check[gems[l]] -= 1
                if check[gems[l]] == 0:
                    cnt -= 1
                l += 1

    answer = sorted(answer, key=lambda x: (x[1]-x[0], x[0], x[1]))
    return answer[0]
