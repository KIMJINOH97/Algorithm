def solution(record):
    answer = []
    action = []
    user = {}
    for r in record:
        li = list(r.split())
        action.append(li)
    for a in action:
        if a[0] == 'Enter':
            user[a[1]] = a[2]
            answer.append([a[1], 'Enter'])
        elif a[0] == 'Leave':
            answer.append([a[1], 'Leave'])
        else:
            user[a[1]] = a[2]
    ans = []
    
    for a in answer:
        if a[1] == 'Enter':
            ans.append(user[a[0]] + '님이 들어왔습니다.')
        elif a[1] == 'Leave':
            ans.append(user[a[0]] + '님이 나갔습니다.')

    return ans