from sys import stdin
N, num = int(stdin.readline()), list(
    map(int, stdin.readline().split()))
op = list(map(int, stdin.readline().split()))

how = []
operator = ['+', '-', '*', '/']
for i, o in enumerate(op):
    for j in range(o):
        how.append(operator[i])

c, check = [], [0 for i in range(len(how))]
cal = []


def permu(n):
    if len(c) == n:
        cal.append(list(c))
        return
    for i in range(len(how)):
        if check[i] == 0:
            check[i] = 1
            c.append(how[i])
            permu(n)
            check[i] = 0
            c.pop()


permu(N-1)

result_max, result_min = -1000000000, 1000000000
for c in cal:
    sum = num[0]
    for i in range(len(c)):
        if c[i] == '+':
            sum += num[i+1]
        if c[i] == '-':
            sum -= num[i+1]
        if c[i] == '*':
            sum *= num[i+1]
        if c[i] == '/':
            if sum < 0:
                sum = -(abs(sum) // num[i+1])
            else:
                sum //= num[i+1]
    if sum > result_max:
        result_max = sum
    if sum < result_min:
        result_min = sum

print(result_max)
print(result_min)
