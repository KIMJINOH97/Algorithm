arr = list(map(int, input().split()))

def merge(left, right):
    i=0
    j=0
    sorted = []
    while (i<len(left)) & (j<len(right)):
        if left[i] < right[j]:
            sorted.append(left[i])
            i+=1
        else:
            sorted.append(right[j])
            j+=1
    while (i<len(left)):
        sorted.append(left[i])
        i+=1

    while(j<len(right)):
        sorted.append(right[j])
        j+=1

    return sorted

def mgsort(lst):
    if len(lst) <=1:
        return lst
    mid = len(lst)//2
    left = lst[:mid]
    right = lst[mid:]

    l = mgsort(left)
    r = mgsort(right)
    return merge(l, r)

print(mgsort(arr))