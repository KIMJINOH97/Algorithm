def solution(play_time, adv_time, logs):
    answer = [0, 0]
    new_log = []

    def change_second(time):
        hour, minute, second = time.split(':')
        return 3600*int(hour) + 60*int(minute) + int(second)

    def int_to_str(time):
        h = time // 3600
        h = '0' + str(h) if h < 10 else str(h)
        time = time % 3600
        m = time // 60
        m = '0' + str(m) if m < 10 else str(m)
        time = time % 60
        s = '0' + str(time) if time < 10 else str(time)
        return h + ':' + m + ':' + s

    for log in logs:
        start, end = log.split('-')
        new_log.append([change_second(start), change_second(end)])

    play_time, adv_time = change_second(play_time), change_second(adv_time)

    ad = [0 for i in range(360000)]
    for log in new_log:
        start, end = log[0], log[1]
        ad[start] += 1
        ad[end] -= 1

    l, r = 0, adv_time
    su = 0

    for i in range(1, play_time+1):
        ad[i] += ad[i-1]

    for i in range(1, play_time+1):
        ad[i] += ad[i-1]

    su = ad[adv_time]
    index = 0
    for i in range(adv_time, play_time+1):
        m = ad[i] - ad[i-adv_time]
        if m > su:
            su = m
            index = i-adv_time+1

    return int_to_str(index)
