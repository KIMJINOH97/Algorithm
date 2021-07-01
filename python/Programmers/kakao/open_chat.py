def solution(record):
    answer = []
    dic = {}
    for r in record:
        content = r.split()
        active, user, nick = content[0], content[1], ''
        if len(content) == 3:
            nick = content[2]
        if active == 'Enter':
            dic[user] = nick
            answer.append((user, "님이 들어왔습니다."))
        elif active == 'Leave':
            answer.append((user, "님이 나갔습니다."))
        else:  # 이름 변경
            dic[user] = nick

    answer = list(map(lambda x: dic[x[0]] + x[1], answer))

    return answer
