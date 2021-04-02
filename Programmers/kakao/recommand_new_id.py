import re


def solution(new_id):
    new_id = new_id.lower()

    p = re.compile('[a-zA-Z0-9]+|[.]+|_|-')
    tmp_id = p.findall(new_id)
    for i, tmp in enumerate(tmp_id):
        if tmp_id[i][0] == '.':
            tmp_id[i] = '.'
    tmp_id = ''.join(tmp_id)
    tmp_id = tmp_id.strip('.')

    if len(tmp_id) == 0:
        tmp_id += "a"
    new_id = tmp_id
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]

    if len(new_id) <= 2:
        k = new_id[-1]
        new_id += k*(3-len(new_id))

    return new_id
