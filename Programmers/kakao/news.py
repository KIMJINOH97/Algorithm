N = 65536
def delete(str1):
    return str1.isalpha()

def solution(str1, str2):
    answer = 0
    str1, str2 = str1.lower(), str2.lower()
    A, B = [], []
    two(str1, A)
    two(str2, B)
    A, B = list(filter(delete, A)), list(filter(delete, B))
    if A == [] and B == []: return N
    A_set, B_set = set(A), set(B)
    inter, union = list(A_set & B_set), list(A_set | B_set)
    inter_count, union_count = 0, 0
    for a in inter:
        inter_count += min(A.count(a), B.count(a))
    for a in union:
        union_count += max(A.count(a), B.count(a))
    
    return int(inter_count/union_count*N)

def two(str1, A):
    for i, s in enumerate(str1):
        if i ==0: continue
        st = str1[i-1]+s
        A.append(st)