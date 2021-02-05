from sys import stdin
import operator

st = stdin.readline
N, li = int(st()), []
dic = {}
sum_num = 0
for i in range(N):
    a = int(st())
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
    sum_num += a
    li.append(a)

li.sort()
sdic = sorted(dic, key=lambda x: (dic[x], x))
m = []
for key in dic:
    if dic[key] == dic[sdic[-1]]:
        m.append(key)

m.sort()
min_num, max_num, mid_num = li[0], li[-1], li[N//2]
least_count, most_count = 0, 0
print(int(round(sum_num/N, 0)))
print(mid_num)
if len(m) < 2:
    print(m[0])
else:
    print(m[1])
print(abs(max_num-min_num))
