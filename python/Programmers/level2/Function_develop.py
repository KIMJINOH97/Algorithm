def solution(progress, speeds):
    answer = []
    how_days = []
    for i in range(len(progress)):
        sp = speeds[i]
        remain = 100 - progress[i]
        day = remain // sp
        if remain % sp != 0:
            day += 1
        how_days.append(day)
    complete_day = how_days[0]
    complete = 0
    for d in how_days:
        if d <= complete_day:
            complete += 1
        else:
            answer.append(complete)
            complete = 1
            complete_day = d
    answer.append(complete)
    return answer