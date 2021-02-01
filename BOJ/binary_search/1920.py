from sys import stdin

N = int(stdin.readline())
li = list(map(int, stdin.readline().split()))
li.sort()


def bin_search(k):
    l = 0
    r = N-1
    while l <= r:
        mid = (l+r)//2
        if li[mid] == k:
            return 1
        if li[mid] < k:
            l = mid+1
        else:
            r = mid-1
    return 0


n, l = int(stdin.readline()), list(map(int, stdin.readline().split()))

for a in l:
    print(bin_search(a))
