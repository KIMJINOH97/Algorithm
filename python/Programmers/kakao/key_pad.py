def solution(numbers, hand):
    answer = ''

    key_pad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], ['*', 0, '#']]
    dic = {}
    for i in range(4):
        for j in range(3):
            dic[key_pad[i][j]] = (i, j)

    left, right = dic['*'], dic['#']

    for n in numbers:
        if n in [1, 4, 7]:
            left = dic[n]
            answer += 'L'
            continue

        if n in [3, 6, 9]:
            right = dic[n]
            answer += 'R'
            continue

        right_r, right_c = right
        left_r, left_c = left
        num_r, num_c = dic[n]

        dist_right = abs(num_r - right_r) + abs(num_c - right_c)
        dist_left = abs(num_r - left_r) + abs(num_c - left_c)

        if dist_right > dist_left:
            left = dic[n]
            answer += 'L'
        elif dist_right < dist_left:
            right = dic[n]
            answer += 'R'
        else:
            if hand == 'right':
                right = dic[n]
                answer += 'R'
            else:
                left = dic[n]
                answer += 'L'

    return answer
