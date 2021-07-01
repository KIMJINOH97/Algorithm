def solution(s):
    answer = len(s)
    l_s = len(s)
    max_slice = len(s) // 2
    for i in range(1, max_slice+1):
        compress = [s[j:j+i] for j in range(0, l_s, i)]
        pre = compress[0]
        cnt = 1
        c_str = ""
        for j in range(1, len(compress)):
            if pre == compress[j]:
                cnt += 1
            else:
                if cnt != 1:
                    c_str += str(cnt)+pre
                else:
                    c_str += pre
                cnt = 1
                pre = compress[j]

        if cnt != 1:
            c_str += str(cnt)+pre
        else:
            c_str += pre
        if len(c_str) < answer:
            answer = len(c_str)

    return answer
