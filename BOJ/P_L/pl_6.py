import re
p = re.compile("(100+1+|01)+$")
N = int(input())
mlist = []
for i in range(0,N):
    m = p.match(input())
    mlist.append(m)
for j in mlist:
    if j:
        print("DANGER")
    else:
        print("PASS")