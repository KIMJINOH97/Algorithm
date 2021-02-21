def solution(s):
    answer = 1

    def is_ok(str1):
        if str1 == str1[::-1]:
            return True
        return False

    N = len(s)
    for i in range(N, 1, -1):
        for j in range(len(s)):
            if j + i > len(s):
                break
            str1 = s[j: j+i]
            if is_ok(str1):
                answer = i
                break
        if answer != 1:
            break

    return answer
