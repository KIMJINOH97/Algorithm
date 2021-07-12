def solution(string):
    answer = ""
    
    dic = {"zero" : "0", "one" : "1",  "two" : "2", "three" : "3", "four" : "4", "five" : "5", "six" :            "6", "seven" : "7", "eight" : "8", "nine" : "9"}
    
    stack = ""
    
    for st in string:
        if st.isdigit():
            answer += st
            continue
        
        stack += st
        if stack in dic:
            answer += dic[stack]
            stack = ""
    
    return int(answer)