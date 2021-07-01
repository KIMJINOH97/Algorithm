import sys

sys.setrecursionlimit(5000)


def solution(nodeinfo):
    answer = [[], []]
    node = []

    for i, n in enumerate(nodeinfo):
        n.append(i+1)
        node.append(n)
    node = sorted(node, key=lambda x: (-x[1], x[0]))

    def divide(arr):
        if len(arr) <= 1:
            if len(arr) > 0:
                answer[0].append(arr[0][2])
                answer[1].append(arr[0][2])
            return arr
        left, right = [], []
        pivot = arr[0]
        answer[0].append(pivot[2])
        for a in arr:
            if a[0] < pivot[0]:
                left.append(a)
            elif a[0] > pivot[0]:
                right.append(a)
        quick = divide(left) + [pivot] + divide(right)
        answer[1].append(pivot[2])
        return quick
    divide(node)
    return answer
