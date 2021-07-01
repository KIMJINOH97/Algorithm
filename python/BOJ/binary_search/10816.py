from sys import stdin

N, li = int(stdin.readline()), list(map(int, stdin.readline().split()))
n, what = int(stdin.readline()), list(map(int, stdin.readline().split()))
li.sort()
aws = sorted(list(set(li)))
dic = {key: 0 for key in aws}
for l in li:
    dic[l] += 1


def bin_search(k):
    l = 0
    r = len(aws)-1
    while l <= r:
        mid = (l+r)//2
        if aws[mid] == k:
            return k
        if aws[mid] < k:
            l = mid+1
        else:
            r = mid - 1
    return -99999999


for w in what:
    ans = bin_search(w)
    if ans == -99999999:
        print("0", end=" ")
    else:
        print(dic[ans], end=" ")
