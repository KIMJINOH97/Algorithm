def solution(n, arr1, arr2):
    l_arr = len(arr1)
    answer = ['' for i in range(l_arr)]

    def make_binary(num):
        binary = ''
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        for i in range(l_arr-len(binary)):
            binary = '0' + binary
        return binary

    for i in range(l_arr):
        arr1[i] = make_binary(arr1[i])
        arr2[i] = make_binary(arr2[i])
        for j in range(l_arr):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                answer[i] += '#'
            else:
                answer[i] += ' '

    return answer
