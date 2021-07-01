from sys import stdin, stdout
a = []
sentance, li = [], []
while True:
    a = stdin.readline()
    if a == '.\n':
        stdout.flush()
        break
    sentance.append(list(a))
stack = []
answer = []


for str1 in sentance:
    stack = []
    for st in str1:
        if st == '(':
            stack.append(1)
        elif st == ')':
            if len(stack) == 0:
                answer.append('no')
                break
            k = stack.pop()
            if not k == 1:
                answer.append('no')
                break
        if st == '[':
            stack.append(2)
        elif st == ']':
            if len(stack) == 0:
                answer.append('no')
                break
            k = stack.pop()
            if not k == 2:
                answer.append('no')
                break
    else:
        if len(stack) == 0:
            answer.append('yes')
        else:
            answer.append('no')


for a in answer:
    print(a)
