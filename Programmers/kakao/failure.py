def solution(N, stages):
    failure = [[0, i+1] for i in range(N)]

    stages.sort()
    pre, start, count = stages[0], 0, 0
    for i, stage in enumerate(stages):
        if not pre == stage:
            challenge_player = len(stages)-start
            clear_player = count
            fail = clear_player / challenge_player
            failure[pre-1][0] = fail
            pre = stage
            start = i
            count = 1
        else:
            count += 1
    if pre <= N:
        failure[pre-1][0] = count / (len(stages) - start)

    failure = sorted(failure, key=lambda x: (-x[0], x[1]))
    answer = []
    for fail in failure:
        answer.append(fail[1])

    return answer
