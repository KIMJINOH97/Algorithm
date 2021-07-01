def foo():
    s = []
    s.append((lec[0][0], lec[0][1], lec[0][2]))
    for i in range(1, N):
        if lec[i][0] >= s[-1][1]:
            s.append((lec[i][0], lec[i][1], lec[i][2]))
        elif lec[i][1] < s[-1][1]:
            s.pop()
            s.append((lec[i][0], lec[i][1], lec[i][2]))
    print(len(s))
    s.sort(key=lambda x: x[0])
    b = []
    for i in range(len(s)):
        b.append(s[i][2])
    print(b)

N = int(input())
lec = []
for i in range(0,N):
    l, A, B = list(map(int, input().split()))
    lec.append((A,B,l))
lec.sort()
foo()