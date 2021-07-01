def solution(lines):
    answer = 0
    traffic = []

    def change_clock(c):
        hour, minute, second = map(float, c.split(':'))
        total = 1000*(hour*3600 + minute*60 + second)
        return int(total)

    for line in lines:
        li = line.split()[1:]
        clock, t = li
        time = int(float(t[:-1])*1000)-1
        end = change_clock(clock)
        if time < 3000:
            start = end - time
        else:
            end = start - 2999
        traffic.append((start, end, clock, t))

    traffic = sorted(traffic)
    t_len = len(traffic)

    for i, tr in enumerate(traffic):
        s, e, a, b = tr
        limit = s - 999
        cnt = 1

        for j in range(i-1, -1, -1):
            next_s, next_e, c, d = traffic[j]
            if next_e >= limit:
                cnt += 1

        if cnt > answer:
            answer = cnt

    return answer
