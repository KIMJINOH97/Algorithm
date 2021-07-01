def solution(arr1, arr2):
    answer = []
    for a, b in zip(arr1, arr2):
        k = []
        for a1, b1 in zip(a, b):
            k.append(a1 + b1)
        answer.append(k)

    return answer
