from collections import deque


def solution(n, t, m, timetable):

    START_TIME = 540
    LAST_BUS_TIME = START_TIME + (n-1) * t

    def changeMinute(t):
        hour, minute = map(int, t.split(":"))
        return 60 * hour + minute

    def changeClock(t):
        hour = t // 60
        minute = t - 60 * hour

        if hour < 10:
            hour = "0" + str(hour)

        if minute < 10:
            minute = "0" + str(minute)

        return str(hour) + ":" + str(minute)

    timetable = sorted(list(map(lambda x: changeMinute(x), timetable)))

    q = deque()

    for time in timetable:
        q.append(time)

    presentBusTime = START_TIME

    while presentBusTime <= LAST_BUS_TIME:
        loadAble = m
        while q and loadAble:
            time = q[0]
            if time > presentBusTime:
                break
            time = q.popleft()
            loadAble -= 1

            if loadAble == 0 and presentBusTime == LAST_BUS_TIME:
                return changeClock(time - 1)

        if len(q) == 0:
            break

        presentBusTime += t

    return changeClock(LAST_BUS_TIME)
