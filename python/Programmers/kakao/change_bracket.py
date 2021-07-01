def solution(p):
    def is_right(st):  # 올바른 괄호 문자열 인지
        right = 0
        for s in st:
            if right < 0:
                return False
            if s == '(':
                right += 1
            else:
                right -= 1
        return True

    if is_right(p):
        return p

    def divide_uv(st):  # u,v로 분리
        right = 0
        for i, s in enumerate(st):
            if s == '(':
                right += 1
            else:
                right -= 1
            if right == 0:
                return i

    def ans(st):
        if st == '':
            return st
        u_i = divide_uv(st) + 1
        u, v = st[:u_i], st[u_i:]
        if is_right(u):
            # answer+=u
            return u+ans(v)
        else:
            empty = '('
            result = ans(v)
            empty += result
            empty += ')'
            u = u[1:-1]
            change_u = ''
            for s in u:
                if s == '(':
                    change_u += ')'
                else:
                    change_u += '('
            return empty+change_u

    return ans(p)
