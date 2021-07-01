import heapq

def solution(jobs):
    answer = 0
    job_len = len(jobs)
    jobs.sort()
    min_job= []
    time = 0
    run= []
    service = 1
    is_start = 0
    while True:
        if len(jobs) == 0 and len(min_job) == 0 and is_start==0:
            break
            
        while len(jobs) != 0 and jobs[0][0] == time:  # 현재시간과 같은 job 대입 
            heapq.heappush(min_job, [jobs[0][1], jobs[0][0]])
            jobs.pop(0)

        if is_start == 1 and service == run[0]: # 프로세스 수행 끝
            is_start = 0
            service=1
            answer += time - run[1]
            run.pop(0)
        
        if is_start == 1:
            service+=1 # 수행시간 증가
            time+=1
            continue
            
        if len(min_job) != 0:
            run = heapq.heappop(min_job) # 돌아가야할 프로세스 pop
            is_start=1
        
        time += 1
    return answer//job_len