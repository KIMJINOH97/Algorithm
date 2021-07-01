def solution(str1, str2):
    N = 65536

    def two(arr):
        J_arr = []
        for i in range(len(arr)-1):
            if (arr[i].isalpha()) and (arr[i+1].isalpha()):
                J_arr.append(arr[i]+arr[i+1])
        return J_arr

    def J(arr1, arr2):
        set_arr1, set_arr2 = set(arr1), set(arr2)
        inter, union = set_arr1 & set_arr2, set_arr1 | set_arr2
        J_inter, J_union = 0, 0
        for s in inter:  # sum함수 안썼을 때
            min_s = min(arr1.count(s), arr2.count(s))
            J_inter += min_s
        # sum함수 썼는데 가독성이 좋아보이진 않음 그래도 코드 줄여줄 수 있어 좋은것같음
        J_union = sum([max(arr1.count(st), arr2.count(st)) for st in union])

        return int((J_inter/J_union)*N) if J_union != 0 else N

    arr1_J, arr2_J = list(str1.lower()), list(str2.lower())
    return J(two(arr1_J), two(arr2_J))
