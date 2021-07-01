def upcount(go):
    for i in range(len(go)):
        go[i][1] += 1

def solution(bl, weight, truck_weights):
    answer = 0
    go=[]
    sum = 0
    for truck in truck_weights:
        upcount(go)
        answer+=1
        if len(go) == 0:
            go.append([truck, 0])
            sum += truck
            continue
        if go[0][1] == bl:
            sum -= go[0][0]
            go.pop(0)            
        if sum+truck <= weight:
            go.append([truck, 0])
            sum+=truck
            continue
        else:
            while sum+truck > weight :
                upcount(go)
                answer += 1
                if go[0][1] == bl:
                    sum-=go[0][0]
                    go.pop(0)
                
        go.append([truck,0])
        sum += truck    
    answer+=bl
    return answer