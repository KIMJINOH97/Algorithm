from copy import deepcopy

answer = False


def solution(key, lock):

    #    start_r, start_c = 0, 0
    lock_N, key_N = len(lock), len(key)

    def rotate_90():
        new_key = [[0 for j in range(key_N)] for i in range(key_N)]
        for i in range(key_N):
            for j in range(key_N-1, -1, -1):
                new_key[i][abs(j-(key_N-1)) % key_N] = key[j][i]
        return new_key

    def is_ok(r, c):
        global answer
        ok = deepcopy(lock)
        for i in range(key_N):
            for j in range(key_N):
                if 0 <= i+r < lock_N and 0 <= j+c < lock_N:
                    ok[i+r][j+c] += key[i][j]

        for i in range(lock_N):
            for j in range(lock_N):
                if ok[i][j] == 0 or ok[i][j] == 2:
                    return False
        answer = True
        return

    for i in range(-key_N+1, lock_N):
        if answer == True:
            break
        for j in range(-key_N+1, lock_N):
            if answer == True:
                break
            for k in range(4):
                key = deepcopy(rotate_90())
                is_ok(i, j)

    return answer
