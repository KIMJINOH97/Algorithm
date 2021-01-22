column = [] #검사할 열
check = [0 for i in range(8)]

def combi(n, result, c_l, start, count):
    if count == n:
        column.append(result)
        return
    for i in range(start, c_l):
        if check[i] == 0:
            check[i] = 1
            combi(n, result+str(i), c_l, i+1, count+1)
            check[i] = 0

def solution(relation):
    answer = 0
    column_len = len(relation[0])
    least = [] # 최소성 만족하는 집합
    for i in range(1, column_len+1):
        combi(i, "", column_len, 0, 0)
    print(column)
    for st in column:
        li = []
        flag = False
        for j in least:
            #if j in st: break
            a, b = set(j), set(st)
            if a&b == a: break  
        else:        
            for r in relation:
                str1 = ""
                for s in st: str1 += r[int(s)]
                li.append(str1)
            copy = list(set(li))
            if len(copy) == len(relation):
                least.append(st)
                answer+=1
            
    return answer