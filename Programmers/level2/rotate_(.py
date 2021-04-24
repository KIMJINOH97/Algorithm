def solution(s):
    answer = 0
    if len(s) % 2 == 1:
        return 0
    dic = {'{': '}', '(': ')', '[': ']'}

    def is_right(s):
        stack = []
        for st in s:
            if len(stack) == 0:
                stack.append(st)
            else:
                if stack[-1] not in dic:
                    stack.append(st)
                elif dic[stack[-1]] == st:
                    stack.pop()
                else:
                    stack.append(st)

        if len(stack) == 0:
            return True
        else:
            return False
    l_s = len(s)
    for i in range(l_s):
        s = s[1:] + s[0]
        if is_right(s):
            answer += 1

    return answer
