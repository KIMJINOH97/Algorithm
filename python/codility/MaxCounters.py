def solution(N, A):
    counters = [0 for i in range(N+1)]

    preMaxCount, maxCount = 0, 0

    for X in A:
        if X == N+1:
            preMaxCount = maxCount
            continue

        if preMaxCount <= counters[X]:  # increase X
            counters[X] += 1
            maxCount = max(maxCount, counters[X])
        else:
            counters[X] = preMaxCount + 1
            maxCount = max(maxCount, counters[X])

    for i in range(1, N+1):
        if counters[i] < preMaxCount:
            counters[i] = preMaxCount

    return counters[1:]
