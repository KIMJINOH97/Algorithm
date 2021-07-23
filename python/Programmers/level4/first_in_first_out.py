def solution(n, cores):
    answer = 0

    l, r = 0, cores[0] * n

    while l <= r:
        mid = (l+r) // 2

        same, cnt = 0, 0
        for core in cores:
            if cnt >= n:
                break
            mok, remain = mid // core, mid % core
            if remain == 0:
                cnt += mok
                same += 1
            else:
                cnt += mok + 1

        if cnt >= n:
            r = mid-1
        else:
            if same + cnt < n:
                l = mid+1
            else:
                a = 0
                index = 0
                for core in cores:
                    remain = mid % core
                    if remain == 0:
                        a += 1
                    if a == n - cnt:
                        return index+1
                    index += 1

    return answer
