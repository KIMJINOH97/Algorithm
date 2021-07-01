def solution(number, k):
    answer = ''
    answer += number[0]
    num_len = len(number)
    limit = num_len-k
    for i in range(1, num_len):
        remain = num_len-i
        if len(answer)+remain == limit:
            answer += number[i]
            continue
        if number[i] <= answer[-1]:
            if len(answer) != limit:
                answer += number[i]
                cmp = number[i]
                continue
        else:
            while True:
                if len(answer) + remain == limit or len(answer) == 0 or answer[-1]>=number[i]:
                    answer+=number[i]
                    break
                answer = answer[:-1]
 
    return answer