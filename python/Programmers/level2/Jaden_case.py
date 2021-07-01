def solution(s):
    answer = ''
    s = s.lower()
    blank = 1
    for i in range(len(s)):
        if s[i] == ' ':
            answer+=' ';
            blank = 1
        elif blank == 1:
            answer+= s[i].upper()
            blank=0
        else:
            answer+=s[i]
    return answer