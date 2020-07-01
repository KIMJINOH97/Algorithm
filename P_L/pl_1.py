def binsearch(lst, low, high, n):
    while low<=high:
        mid = int((low+high)/2)
        if lst[mid] == n:
            return mid
        elif lst[mid]<n:
            low = mid+1
        else:
            high = mid-1
    return -1
            
bslist = list(map(int, input().split()))
bslist.sort()
N = int(input())
ans = binsearch(bslist, 0, len(bslist)-1, N)
if ans == -1:
    print("None")
else:
    print(ans+1)