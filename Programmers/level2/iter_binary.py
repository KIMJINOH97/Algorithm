def solution(s):
    answer = []
    def binary(n):
        st = ""
        while n != 0:
            st = str(n%2)+ st
            n = n//2
        return st
    z = 0
    i = 0
    
    while s != '1':
        z += s.count('0')
        li = list(filter(lambda x: x != '0', list(s)))
        s = binary(len(li))
        i += 1
        
    return [i,z]