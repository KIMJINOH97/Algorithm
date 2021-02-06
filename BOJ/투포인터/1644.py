from sys import stdin

std = stdin.readline
N = int(std())

number = [0 for i in range(N+1)]
prime = []

for i in range(2, N+1):
    if number[i] == 1:
        continue
    for j in range(i+i, N+1, i):
        if number[j] == 0:
            number[j] = 1

for i in range(2, N+1):
    if number[i] == 0:
        prime.append(i)

if N < 3:
    print(N-1)
else:
    l, r = 0, 1
    prime_sum = 5
    answer = 0
    while l <= r:
        if l == r:
            if prime_sum == N:
                answer += 1
                break
        if prime_sum == N:
            answer += 1
            prime_sum -= prime[l]
            l += 1
        elif prime_sum < N:
            r += 1
            if r == len(prime):
                break
            prime_sum += prime[r]
        else:
            prime_sum -= prime[l]
            l += 1

    print(answer)
