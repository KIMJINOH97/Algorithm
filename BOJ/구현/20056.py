from sys import stdin
from copy import deepcopy

std = stdin.readline

N, M, K = map(int, std().split())

fire = {}
check = [[0 for i in range(N)] for j in range(N)]

nr, nc = [-1, -1, 0, 1, 1, 1, 0, -1], [0, 1, 1, 1, 0, -1, -1, -1]

for i in range(M):
    r, c, m, s, d = map(int, std().split())
    fire[(r-1, c-1)] = [(m, s, d)]


def move():
    global fire
    fire_dic = {}
    for key in fire:
        f_r, f_c = key
        for f in fire[key]:
            #print(m, s, d)
            m, s, d = f
            r, c = (f_r+nr[d]*s) % N, (f_c+nc[d]*s) % N
            k = (r, c)
            if k in fire_dic:
                fire_dic[k].append((m, s, d))
            else:
                fire_dic[k] = [(m, s, d)]

    new_dic = {}
    for key in fire_dic:
        r, c = key
        if len(fire_dic[key]) > 1:
            flag = fire_dic[key][0][2] % 2
            odd = False
            sum_m = 0
            sum_s = 0
            for k in fire_dic[key]:
                m, s, d = k
                if flag != d % 2:
                    odd = True
                sum_m += m
                sum_s += s
            start = 0
            sum_m //= 5
            sum_s //= len(fire_dic[key])
            if odd == True:
                start = 1
            if sum_m != 0:
                for i in range(start, 8, 2):
                    new_key = (r, c)
                    if new_key in new_dic:
                        new_dic[new_key].append((sum_m, sum_s, i))
                    else:
                        new_dic[new_key] = [(sum_m, sum_s, i)]
        else:
            new_dic[(r, c)] = fire_dic[(r, c)]
    fire = deepcopy(new_dic)
    return


while K > 0:
    K -= 1
    move()


answer = 0

for key in fire:
    for k in fire[key]:
        answer += k[0]

print(answer)
