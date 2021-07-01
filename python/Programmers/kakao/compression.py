def solution(msg):
    answer = []
    dic = {chr(65+i): i+1 for i in range(26)}

    index = 27
    str1 = ""
    for m in msg:
        if str1+m in dic:
            str1 += m
        else:
            dic[str1+m] = index
            index += 1
            answer.append(dic[str1])
            str1 = m

    return answer+[dic[str1]]
