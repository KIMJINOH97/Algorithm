arr = list(map(int, input().split()))
def qsort(lst):
    if len(lst) <=1:
        return lst
    k = len(lst)//2
    pv = lst[k]
    l_lst, eq_lst, r_lst = [], [], []
    for num in lst:
        if num < pv:
            l_lst.append(num)
        elif num > pv:
            r_lst.append(num)
        else:
            eq_lst.append(num)
    return qsort(l_lst) + eq_lst + qsort(r_lst)

print(qsort(arr))