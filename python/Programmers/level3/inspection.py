def solution(n, times):
    answer = 0
    l, r = 1, 1000000000*1000000000
    while l <= r:
        mid = (l+r) // 2
        ans = 0
        for time in times:
            ans += mid // time

        if ans >= n:
            answer = mid
            r = mid-1
        elif ans < n:
            l = mid+1

    return answer
