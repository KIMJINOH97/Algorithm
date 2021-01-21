def solution(msg):
    answer = []
    dic = {}
    for i in range(26): dic[chr(ord('A')+i)] = i+1
    lzw,i, num = 0,0,26
    while len(msg) != lzw:
        add = msg[i]
        for j in range(i+1, len(msg)):
            add+=msg[j]
            if add not in dic: # 긴문자열 찾았을때
                num+=1
                dic[add] = num # 긴문자열 색인번호 등록
                lzw += len(add)-1 # 입력에서 제거
                answer.append(dic[add[:-1]]) # 색인번호 출력
                i += j-i
                break
        else:
            lzw += len(add)
            answer.append(dic[add])
                
    
    return answer