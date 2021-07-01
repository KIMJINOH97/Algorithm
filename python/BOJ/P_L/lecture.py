import queue

pq = queue.PriorityQueue()

def ans():
    for i in range(1,N):
        if pq.queue[0][0] <= lec[i][0]:
            pq.get()
            pq.put((lec[i][1],lec[i][1]))
        else:
            pq.put((lec[i][1],lec[i][1]))
    print(pq.qsize())     
    return

N = int(input())
lec = []
for _ in range(0,N):
    k, A, B = list(map(int, input().split()))
    lec.append((A,B))
lec.sort(key=lambda x: x[0])
pq.put((lec[0][1],lec[0][1]))

ans()