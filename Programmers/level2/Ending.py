def solution(n, words):
    answer = []
    li = []
    for i, word in enumerate(words):
        if i == 0:
            pre = words[0][-1]
            li.append(words[0])
        elif word in li or word[0] != pre:
            answer.append(i%n+1)
            answer.append(i//n + 1)
            break
        else:
            li.append(word)
            pre = word[-1]
    else: return [0,0]
     
    return answer