// 2020 운영체제
// CPU Schedule Simulator Homework
// Student Number : B611050
// Name : 김진오

#include <assert.h>
#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

#define SEED 10

// process states
#define S_IDLE 0
#define S_READY 1
#define S_BLOCKED 2
#define S_RUNNING 3
#define S_TERMINATE 4

int NPROC, NIOREQ, QUANTUM;
// NPROC: 시뮬레이션에 생성될 총 프로세스 수 NIQREQ: 시뮬레이션 중 생성될 총 IO 요청의 수

struct ioDoneEvent {  // IO가 언제 끝나는 지
    int procid;
    int doneTime;
    int len;
    struct ioDoneEvent *prev;
    struct ioDoneEvent *next;
} ioDoneEventQueue, *ioDoneEvent;

struct process {
    int id;
    int len;                // for queue
    int targetServiceTime;  // = procServTime[] 결국 이것 프로세스 수행시간
    int serviceTime;        // 현재 서비스 받은 시간
    int startTime;          // 생성시간
    int endTime;            // 종료시간
    char state;
    int priority;
    int saveReg0, saveReg1;
    struct process *prev;
    struct process *next;
} * procTable;

struct process idleProc;  // idle상태에서 ready queue에 없으면 이 프로세스가 cpu에 할당
struct process readyQueue;
struct process blockedQueue;
struct process *runningProc;

int cpuReg0, cpuReg1;
int currentTime = 0;
int *procIntArrTime, *procServTime, *ioReqIntArrTime, *ioServTime;
// ioServTime = io 작동시간

void compute() {
    // DO NOT CHANGE THIS FUNCTION
    cpuReg0 = cpuReg0 + runningProc->id;
    cpuReg1 = cpuReg1 + runningProc->id;
    // printf("In computer proc %d cpuReg0 %d\n",runningProc->id,cpuReg0);
}

void initProcTable() {
    int i;
    for (i = 0; i < NPROC; i++) {
        procTable[i].id = i;
        procTable[i].len = 0;
        procTable[i].targetServiceTime = procServTime[i];
        procTable[i].serviceTime = 0;
        procTable[i].startTime = 0;
        procTable[i].endTime = 0;
        procTable[i].state = S_IDLE;
        procTable[i].priority = 0;
        procTable[i].saveReg0 = 0;
        procTable[i].saveReg1 = 0;
        procTable[i].prev = NULL;
        procTable[i].next = NULL;
    }
}

struct process *lastReadyQ() {
    struct process *currentReadyQueue = &readyQueue;
    while (readyQueue.len > 0 && currentReadyQueue->next != NULL) {
        currentReadyQueue = currentReadyQueue->next;
    }
    return currentReadyQueue;
}

struct process *lastBlockQ() {
    struct process *currentBlockQueue = &blockedQueue;
    while (blockedQueue.len > 0 && currentBlockQueue->next != NULL) {
        currentBlockQueue = currentBlockQueue->next;
    }
    return currentBlockQueue;
}

void printState(int nproc, int cpu, int qtime) {
    struct process *rp = runningProc;
    int ioDoneTime = INT_MAX;
    int proc = -1;
    int min = INT_MAX;
    struct ioDoneEvent *idq = &ioDoneEventQueue;
    while (ioDoneEventQueue.len > 0 && idq != NULL) {
        if (idq->doneTime < min) {
            ioDoneTime = idq->doneTime;
            proc = idq->procid;
            break;
        }
        idq = idq->next;
    }
    printf("%d processing Proc %d priority: %d servT %d targetServT %d nproc %d cpuUseTime %d qTime %d proc %d ioDoneTime %d ioDoneEvent Length %d \n", currentTime, rp->id, rp->priority, rp->serviceTime, rp->targetServiceTime, nproc, cpu, qtime, proc, ioDoneTime, ioDoneEventQueue.len);
}

void procExecSim(struct process *(*scheduler)()) {
    int pid, qTime = 0, cpuUseTime = 0, nproc = 0, termProc = 0, nioreq = 0;
    char schedule = 0, nextState = S_IDLE;
    int nextForkTime, nextIOReqTime;

    nextForkTime = procIntArrTime[nproc];
    nextIOReqTime = ioReqIntArrTime[nioreq];

    idleProc.id = -1;
    idleProc.targetServiceTime = INT_MAX;
    readyQueue.id = -1;
    blockedQueue.id = -1;
    runningProc = &idleProc;  // 초기 돌아가는 프로세스는 idle

    int qFlag = 0;
    while (1) {
        currentTime++;  // 프로세스 생성 후 타이머
        qTime++;
        runningProc->serviceTime++;
        if (runningProc != &idleProc) cpuUseTime++;  //cpu 사용할 때 동작

        cpuReg0 = runningProc->saveReg0;
        cpuReg1 = runningProc->saveReg1;
        // MUST CALL compute() Inside While loop
        compute();

        runningProc->saveReg0 = cpuReg0;
        runningProc->saveReg1 = cpuReg1;
        //printState(nproc, cpuUseTime, qTime);

        if (currentTime == nextForkTime) { /* CASE 2 : a new process created */
            // readyQueue에 프로세스 넣는 과정
            struct process *currentQueue = lastReadyQ();
            currentQueue->next = &procTable[nproc];  // Queue의 끝에 넣어줌

            procTable[nproc].state = S_READY;
            procTable[nproc].startTime = currentTime;
            readyQueue.len++;
            nextForkTime = currentTime + procIntArrTime[++nproc];
            nextState = S_READY;

            //printf("process %d targetST %d servTime %d added to Ready Queue Next Fork Time %d \n", procTable[nproc-1].id, procTable[nproc-1].targetServiceTime, procTable[nproc-1].serviceTime, nextForkTime);
        }

        if (qTime == QUANTUM) {  // CASE 1 : The quantum expires
            // 현재 돌고 있는 process를 readyqueue에 넣고 스케쥴링
            if (runningProc != &idleProc) {
                nextState = S_READY;
            }
            qFlag = 1;
            runningProc->priority--;
            qTime = 0;
        }

        struct ioDoneEvent *prevIoDoneQ = &ioDoneEventQueue;
        struct ioDoneEvent *currentQ = &ioDoneEventQueue;
        while (ioDoneEventQueue.len > 0 && currentQ->next != NULL) {  // CASE 3 : IO Done Event
            // io끝나는 시간이 현재 시간일 때 blockqueue에서 ready로 후 스케쥴
            prevIoDoneQ = currentQ;
            currentQ = currentQ->next;
            if (currentQ->doneTime == currentTime) {
                pid = currentQ->procid;  // 완료한 프로세스의 id
                prevIoDoneQ->next = currentQ->next;
                ioDoneEventQueue.len--;

                // blockedQueue에서 찾아서 뽑아냄
                struct process *prevBlock = &blockedQueue;
                struct process *currentBlock = &blockedQueue;

                while (blockedQueue.len > 0 && currentBlock->id != pid) {
                    prevBlock = currentBlock;
                    currentBlock = currentBlock->next;
                }
                prevBlock->next = currentBlock->next;
                //printf("cuBlo id : %d Tc: %d\n", currentBlock->id, currentBlock->targetServiceTime);
                currentBlock->next = NULL;
                blockedQueue.len--;

                // blockproc을 readyQueue에 맨끝에 넣어줌
                struct process *currentReadyQueue = lastReadyQ();
                // currentBlock의상태가 terminate라면 그대로 두고 실행 프로세스 ready에 넣음
                if (currentBlock->state == S_TERMINATE) {
                    // 종료상태면  레디에 넣지 않음.
                } else {
                    // blockqueue에서 뽑아낸 것을 ready에 넣음.
                    currentReadyQueue->next = currentBlock;
                    currentBlock->state = S_READY;
                    readyQueue.len++;
                }
                nextState = S_READY;
                qTime = 0;
            }
        }

        if (cpuUseTime == nextIOReqTime && nioreq < NIOREQ) {  // CASE 5: request IO operations (only when the process does not terminate)
            // io가 일어날 때(IO일 때 runP = idle아님) : 현 process block, iodoneQueue에넣고 스케쥴러 호출

            //printf("ioreq  currentTime : %d state : %d\n", currentTime, runningProc->state);
            // blockedQueue에 실행중인 프로세스 넣는다.
            struct process *currentBlock = lastBlockQ();
            currentBlock->next = runningProc;
            blockedQueue.len++;

            // ioDoneEventQueue에 io시작한 것을 넣음
            ioDoneEvent[nioreq].procid = runningProc->id;
            ioDoneEvent[nioreq].doneTime = currentTime + ioServTime[nioreq];  // 현재시간 + io가 동작하는 시간

            struct ioDoneEvent *currentIo = &ioDoneEventQueue;
            while (ioDoneEventQueue.len > 0 && currentIo->next != NULL) {
                currentIo = currentIo->next;
            }
            currentIo->next = &ioDoneEvent[nioreq];

            ioDoneEventQueue.len++;
            nextIOReqTime = cpuUseTime + ioReqIntArrTime[++nioreq];
            nextState = S_BLOCKED;
            qTime = 0;
            if (qFlag != 1) {
                runningProc->priority++;
            }
        }

        if (runningProc->serviceTime == runningProc->targetServiceTime) {  // CASE 4 : the process job done and terminates
            runningProc->endTime = currentTime;
            nextState = S_TERMINATE;
            int diff = runningProc->endTime - runningProc->startTime;
            // printf("runningproc start : %d end : %d  걸린 시간 : %d\n", runningProc->startTime, runningProc->endTime, diff);
            qTime = 0;
        }

        runningProc->state = nextState;  // 현 process state 업데이트

        // 5번째 스케쥴러

        if (nextState == S_TERMINATE) {
            termProc++;
            //printf("**%d-th proc terminated at %d : Process %d\n", termProc, currentTime, runningProc->id);
            runningProc = scheduler();
        }
        if (nextState == S_BLOCKED) {
            runningProc = scheduler();
        }
        if (nextState == S_READY) {
            if (runningProc != &idleProc) {
                struct process *lastReadyQueue = lastReadyQ();
                lastReadyQueue->next = runningProc;
                readyQueue.len++;
            }
            runningProc = scheduler();
            qTime = 0;
        }
        if (runningProc == &idleProc && readyQueue.len > 0) {
            runningProc = scheduler();
        }

        nextState = S_RUNNING;
        runningProc->state = nextState;
        qFlag = 0;

        if (termProc == NPROC && blockedQueue.len == 0) {
            // printf("readyQ len : %d doneQ len : %d blockQ len: %d \n", readyQueue.len, ioDoneEventQueue.len, blockedQueue.len);
            return;
        }
        // printf("%d \n", currentTime);
        // call scheduler() if needed

    }  // while loop
}

// RR,SJF(Modified),SRTN,Guaranteed Scheduling(modified),Simple Feed Back Scheduling
// ready queue중 하나를 뽑아 return
struct process *RRschedule() {
    if (readyQueue.len > 0) {
        struct process *firstQueue = readyQueue.next;
        if (readyQueue.len == 1) {
            readyQueue.next = &readyQueue;
        } else {
            readyQueue.next = readyQueue.next->next;  // 큐의 가장 앞부분을 넘김
            firstQueue->next = NULL;                  // 떨어져 나가면서 링크 끊기
        }
        readyQueue.len--;
        firstQueue->state = S_RUNNING;
        return firstQueue;
    } else {
        idleProc.state = S_RUNNING;
        return &idleProc;
    }
}
struct process *SJFschedule() {
    if (readyQueue.len == 0) {
        idleProc.state = S_RUNNING;
        return &idleProc;
    }

    struct process *prevQueue = readyQueue.next;
    struct process *currentQueue = readyQueue.next;
    int min_time = currentQueue->targetServiceTime;
    int Q_ServiceTime;
    int ppid = currentQueue->id;
    // 최소 시간 프로세스 찾기

    while (currentQueue->next != NULL) {
        prevQueue = currentQueue;
        currentQueue = currentQueue->next;
        Q_ServiceTime = currentQueue->targetServiceTime;
        if (Q_ServiceTime < min_time) {
            min_time = Q_ServiceTime;
            ppid = currentQueue->id;
        }
    }
    prevQueue = &readyQueue;
    currentQueue = &readyQueue;
    while (currentQueue->id != ppid) {
        prevQueue = currentQueue;
        currentQueue = currentQueue->next;
    }

    prevQueue->next = currentQueue->next;
    currentQueue->next = NULL;

    readyQueue.len--;
    currentQueue->state = S_RUNNING;
    return currentQueue;
}
struct process *SRTNschedule() {
    if (readyQueue.len == 0) {
        idleProc.state = S_RUNNING;
        return &idleProc;
    }

    struct process *prevQueue = readyQueue.next;
    struct process *currentQueue = readyQueue.next;
    int min_time = currentQueue->targetServiceTime - currentQueue->serviceTime;
    int diffTime;
    int ppid = currentQueue->id;
    // 최소 시간 프로세스 찾기

    while (currentQueue->next != NULL) {
        prevQueue = currentQueue;
        currentQueue = currentQueue->next;
        diffTime = currentQueue->targetServiceTime - currentQueue->serviceTime;
        if (diffTime < min_time) {
            min_time = diffTime;
            ppid = currentQueue->id;
        }
    }
    prevQueue = &readyQueue;
    currentQueue = &readyQueue;
    while (currentQueue->id != ppid) {
        prevQueue = currentQueue;
        currentQueue = currentQueue->next;
    }

    prevQueue->next = currentQueue->next;
    currentQueue->next = NULL;

    readyQueue.len--;
    currentQueue->state = S_RUNNING;
    return currentQueue;
}
struct process *GSschedule() {
    if (readyQueue.len == 0) {
        idleProc.state = S_RUNNING;
        return &idleProc;
    }

    struct process *prevQueue = readyQueue.next;
    struct process *currentQueue = readyQueue.next;
    double min_time = (double)(currentQueue->serviceTime) / (double)(currentQueue->targetServiceTime);
    double ratioTime;
    int ppid = currentQueue->id;
    // 최소 시간 프로세스 찾기

    while (currentQueue->next != NULL) {
        prevQueue = currentQueue;
        currentQueue = currentQueue->next;
        ratioTime = (double)(currentQueue->serviceTime) / (double)(currentQueue->targetServiceTime);
        if (ratioTime < min_time) {
            min_time = ratioTime;
            ppid = currentQueue->id;
        }
    }

    prevQueue = &readyQueue;
    currentQueue = &readyQueue;
    while (currentQueue->id != ppid) {
        prevQueue = currentQueue;
        currentQueue = currentQueue->next;
    }

    prevQueue->next = currentQueue->next;
    currentQueue->next = NULL;

    readyQueue.len--;
    currentQueue->state = S_RUNNING;
    return currentQueue;
}
struct process *SFSschedule() {
    if (readyQueue.len == 0) {
        idleProc.state = S_RUNNING;
        return &idleProc;
    }

    struct process *prevQueue = readyQueue.next;
    struct process *currentQueue = readyQueue.next;
    int max_priority = currentQueue->priority;
    int currentPriority;
    int ppid = currentQueue->id;
    // 최대 우선순위 프로세스 찾기

    while (currentQueue->next != NULL) {
        prevQueue = currentQueue;
        currentQueue = currentQueue->next;
        currentPriority = currentQueue->priority;
        //printf("current id : %d priority : %d \n", currentQueue->id, currentQueue->priority);
        if (currentPriority > max_priority) {
            max_priority = currentPriority;
            ppid = currentQueue->id;
        }
    }
    prevQueue = &readyQueue;
    currentQueue = &readyQueue;
    while (currentQueue->id != ppid) {
        prevQueue = currentQueue;
        currentQueue = currentQueue->next;
    }

    prevQueue->next = currentQueue->next;
    currentQueue->next = NULL;

    readyQueue.len--;
    currentQueue->state = S_RUNNING;
    return currentQueue;
}

void printResult() {
    // DO NOT CHANGE THIS FUNCTION
    int i, totalWallTime = 0, totalRegValue = 0;
    for (i = 0; i < NPROC; i++) {
        totalWallTime += procTable[i].endTime - procTable[i].startTime;
        /*
                   printf("proc %d serviceTime %d targetServiceTime %d saveReg0 %d\n",
                   i,procTable[i].serviceTime,procTable[i].targetServiceTime, procTable[i].saveReg0);
                   */
        totalRegValue += procTable[i].saveReg0 + procTable[i].saveReg1;
    }
    printf("%d Process processed - Average Wall Clock Service Time : %g Average Two Register Sum Value %g\n",
           NPROC, (float)totalWallTime / NPROC, (float)totalRegValue / NPROC);
}

int main(int argc, char *argv[]) {
    // DO NOT CHANGE THIS FUNCTION
    int i;
    int totalProcServTime = 0, ioReqAvgIntArrTime;
    int SCHEDULING_METHOD, MIN_INT_ARRTIME, MAX_INT_ARRTIME, MIN_SERVTIME, MAX_SERVTIME, MIN_IO_SERVTIME, MAX_IO_SERVTIME, MIN_IOREQ_INT_ARRTIME;

    if (argc < 12) {
        printf("%s: SCHEDULING_METHOD NPROC NIOREQ QUANTUM MIN_INT_ARRTIME MAX_INT_ARRTIME MIN_SERVTIME MAX_SERVTIME MIN_IO_SERVTIME MAX_IO_SERVTIME MIN_IOREQ_INT_ARRTIME\n", argv[0]);
        exit(1);
    }

    SCHEDULING_METHOD = atoi(argv[1]);
    NPROC = atoi(argv[2]);
    NIOREQ = atoi(argv[3]);
    QUANTUM = atoi(argv[4]);
    MIN_INT_ARRTIME = atoi(argv[5]);  // 프로세스 생성 시 사용되는 process interarrival time 최소
    MAX_INT_ARRTIME = atoi(argv[6]);
    MIN_SERVTIME = atoi(argv[7]);  // 각 프로세스에 할당 된 수행시간의 최소 값
    MAX_SERVTIME = atoi(argv[8]);
    MIN_IO_SERVTIME = atoi(argv[9]);  // 각 IO요청이 발생 했을 때 이 요청이 완료되기 위해 필요한 최소값
    MAX_IO_SERVTIME = atoi(argv[10]);
    MIN_IOREQ_INT_ARRTIME = atoi(argv[11]);

    printf("SIMULATION PARAMETERS : SCHEDULING_METHOD %d NPROC %d NIOREQ %d QUANTUM %d \n", SCHEDULING_METHOD, NPROC, NIOREQ, QUANTUM);
    printf("MIN_INT_ARRTIME %d MAX_INT_ARRTIME %d MIN_SERVTIME %d MAX_SERVTIME %d\n", MIN_INT_ARRTIME, MAX_INT_ARRTIME, MIN_SERVTIME, MAX_SERVTIME);
    printf("MIN_IO_SERVTIME %d MAX_IO_SERVTIME %d MIN_IOREQ_INT_ARRTIME %d\n", MIN_IO_SERVTIME, MAX_IO_SERVTIME, MIN_IOREQ_INT_ARRTIME);

    srandom(SEED);

    // allocate array structures
    procTable = (struct process *)malloc(sizeof(struct process) * NPROC);  // PCB
    ioDoneEvent = (struct ioDoneEvent *)malloc(sizeof(struct ioDoneEvent) * NIOREQ);
    procIntArrTime = (int *)malloc(sizeof(int) * NPROC);
    procServTime = (int *)malloc(sizeof(int) * NPROC);
    ioReqIntArrTime = (int *)malloc(sizeof(int) * NIOREQ);
    ioServTime = (int *)malloc(sizeof(int) * NIOREQ);

    // initialize queues
    readyQueue.next = readyQueue.prev = &readyQueue;

    blockedQueue.next = blockedQueue.prev = &blockedQueue;
    ioDoneEventQueue.next = ioDoneEventQueue.prev = &ioDoneEventQueue;
    ioDoneEventQueue.doneTime = INT_MAX;
    ioDoneEventQueue.procid = -1;
    ioDoneEventQueue.len = readyQueue.len = blockedQueue.len = 0;

    // generate process interarrival times
    for (i = 0; i < NPROC; i++) {
        procIntArrTime[i] = random() % (MAX_INT_ARRTIME - MIN_INT_ARRTIME + 1) + MIN_INT_ARRTIME;
    }

    // assign service time for each process
    for (i = 0; i < NPROC; i++) {
        procServTime[i] = random() % (MAX_SERVTIME - MIN_SERVTIME + 1) + MIN_SERVTIME;
        totalProcServTime += procServTime[i];
    }

    ioReqAvgIntArrTime = totalProcServTime / (NIOREQ + 1);

    // generate io request interarrival time
    for (i = 0; i < NIOREQ; i++) {
        ioReqIntArrTime[i] = random() % ((ioReqAvgIntArrTime - MIN_IOREQ_INT_ARRTIME) * 2 + 1) + MIN_IOREQ_INT_ARRTIME;
    }

    // generate io request service time
    for (i = 0; i < NIOREQ; i++) {
        ioServTime[i] = random() % (MAX_IO_SERVTIME - MIN_IO_SERVTIME + 1) + MIN_IO_SERVTIME;
    }

#ifdef DEBUG
    // printing process interarrival time and service time
    printf("Process Interarrival Time :\n");
    for (i = 0; i < NPROC; i++) {
        printf("%d ", procIntArrTime[i]);
    }
    printf("\n");
    printf("Process Target Service Time :\n");
    for (i = 0; i < NPROC; i++) {
        printf("%d ", procTable[i].targetServiceTime);
    }
    printf("\n");
#endif

    // printing io request interarrival time and io request service time
    printf("IO Req Average InterArrival Time %d\n", ioReqAvgIntArrTime);
    printf("IO Req InterArrival Time range : %d ~ %d\n", MIN_IOREQ_INT_ARRTIME,
           (ioReqAvgIntArrTime - MIN_IOREQ_INT_ARRTIME) * 2 + MIN_IOREQ_INT_ARRTIME);

#ifdef DEBUG
    printf("IO Req Interarrival Time :\n");
    for (i = 0; i < NIOREQ; i++) {
        printf("%d ", ioReqIntArrTime[i]);
    }
    printf("\n");
    printf("IO Req Service Time :\n");
    for (i = 0; i < NIOREQ; i++) {
        printf("%d ", ioServTime[i]);
    }
    printf("\n");
#endif

    struct process *(*schFunc)();  // 함수형 포인터: 함수의 주소를 저장
    switch (SCHEDULING_METHOD) {
        case 1:
            schFunc = RRschedule;
            break;
        case 2:
            schFunc = SJFschedule;
            break;
        case 3:
            schFunc = SRTNschedule;
            break;
        case 4:
            schFunc = GSschedule;
            break;
        case 5:
            schFunc = SFSschedule;
            break;
        default:
            printf("ERROR : Unknown Scheduling Method\n");
            exit(1);
    }

    initProcTable();
    procExecSim(schFunc);
    printResult();
}
