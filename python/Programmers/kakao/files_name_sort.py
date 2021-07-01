import re

def solution(files):
    p = re.compile('[a-zA-z\-.\s]+')
    q = re.compile('[0-9]+')
    answer = []
    files = sorted(files, key=lambda x: (p.findall(x)[0].lower(), int(q.findall(x)[0])))
    print(files)

    return files