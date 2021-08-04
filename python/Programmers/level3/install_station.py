def solution(n, stations, w):
    answer = 0
    now = 1
    
    def count5G(fiveRange):
        cnt = fiveRange // (2*w + 1)
        if fiveRange % (2*w +1) != 0:
            cnt += 1
        return cnt
    
    for station in stations:
        # left ~ right 까지 설치해야함
        left, right = now, station - w - 1
        if right < left:
            now = station + w + 1
            continue
        fiveRange = right - left + 1
        cnt = count5G(fiveRange)
        answer += cnt
        now = station + w + 1
    
    if now <= n: # 마지막에 빈 자리가 있을 때도 봐야함
        answer += count5G(n - now + 1)

    return answer