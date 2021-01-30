def solution(lines):
    answer = 0
    traffic = []
    m = []
    for line in lines:
        li = line.split()
        li.pop(0)
        time = list(map(float, li[0].split(':')))
        total_time = int(1000*(3600*time[0] + 60*time[1] + time[2]))
        ing = int(1000*float(li[1][:-1]))
        if total_time < 3000:
            traffic.append([total_time - ing, total_time])
            continue
        if ing >= 3000:
            li[0] = total_time - 2999
        else:
            li[0] = total_time-ing+1
        li[1] = total_time
        traffic.append(li)

    traffic = sorted(traffic, key=lambda x: x[0])
    for tr in traffic:
        if len(m) == 0:
            m.append(tr[1])
            if answer < len(m):
                answer = len(m)
            continue
        m.append(tr[1])
        new_m = []
        for i in range(len(m)):
            if m[i] >= tr[0]-999:
                new_m.append(m[i])
        m = new_m
        if answer < len(m):
            answer = len(m)

    return answer
