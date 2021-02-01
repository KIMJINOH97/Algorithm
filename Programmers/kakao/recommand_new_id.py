import re


def solution(new_id):
    p = re.compile('[0-9a-zA-Z\-\_\.]+')
    check = p.match(new_id)
    if new_id[-1] != '.' and new_id[0] != '.' and 3 <= len(new_id) <= 15:
        if check and check == new_id:
            return new_id

    new_id = list(new_id)
    for i, s in enumerate(new_id):
        if s.isupper():
            new_id[i] = s.lower()

    new_id = p.findall(str(new_id))
    str1 = ''
    same = False
    for s in new_id:
        if s == '.':
            if same == False:
                str1 += s
                same = True
                continue
            else:
                continue
        else:
            same = False
            str1 += s
    print(str1)

    while True:
        if len(str1) == 0:
            break
        if str1[-1] != '.' and str1[0] != '.':
            break
        if str1[-1] == '.':
            str1 = str1[:-1]
        if len(str1) != 0 and str1[0] == '.':
            str1 = str1[1:]
    if len(str1) == 0:
        str1 += 'a'
    if len(str1) >= 16:
        str1 = str1[:15]

    while True:
        if len(str1) == 0:
            break
        if str1[-1] != '.':
            break
        str1 = str1[:-1]

    if len(str1) <= 2:
        while len(str1) != 3:
            str1 += str1[-1]

    return str1
