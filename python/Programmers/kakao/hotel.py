def solution(k, room_number):
    answer= []
    roomDic = {}
    
    def findRoot(num):
        if num == roomDic[num][0]:
            return num
        
        return findRoot(roomDic[num][0])
    
    for rn in room_number:
        if rn not in roomDic:
            roomDic[rn] = [rn, rn]
            answer.append(rn)
            continue
        
        root = findRoot(rn)
        rt, lastNum = roomDic[root]
        nextNum = lastNum + 1
        while True:
            if nextNum not in roomDic:
                roomDic[nextNum] = [root, nextNum]
                roomDic[root][1] = nextNum
                answer.append(nextNum)
                break
            
            nextRoot, last = roomDic[nextNum]
            roomDic[nextNum][0] = root
            nextNum = last + 1
            
        
    return answer