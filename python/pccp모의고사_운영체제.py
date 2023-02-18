from queue import PriorityQueue

def solution(program):
    exe=0
    answer=[0]*11
    pq=PriorityQueue()
    program.sort(key=lambda x : x[1])
    #print(program)
    cur_time=program[0][1]
    def call():
         while len(program)>0 and cur_time>=program[0][1]:
            #현재시간보다 호출시간 적은것 모두 pq에 넣음
            #print('putin',program[0])
            pq.put(program.pop(0))
    while 1 :
        if pq.empty():
            cur_time=program[0][1]
            call()
        
        exe=pq.get()
        #print(exe,' ',program)
        answer[exe[0]]+=cur_time-exe[1] #대기시간저장
        cur_time+=exe[2]
        #print(answer,'cur=',cur_time)
        if len(program)<=0 and pq.empty():
            answer[0]=cur_time
            break
        call()

    return answer

print(solution([[3, 6, 4], [4, 2, 5], [1, 0, 5], [5, 0, 5]]))



#heapq를 사용하여 속도개선
"""import heapq

def solution(program):
    exe=0
    answer=[0]*11
    pq=[]
    program.sort(key=lambda x : x[1])
    #print(program)
    cur_time=program[0][1]
    def call():
         while len(program)>0 and cur_time>=program[0][1]:
            #현재시간보다 호출시간 적은것 모두 pq에 넣음
            #print('putin',program[0])
            heapq.heappush(pq,program.pop(0))
    while 1 :
        if len(pq)==0:
            cur_time=program[0][1]
            call()
        
        exe=heapq.heappop(pq)
        #print(exe,' ',program)
        answer[exe[0]]+=cur_time-exe[1] #대기시간저장
        cur_time+=exe[2]
        #print(answer,'cur=',cur_time)
        if len(program)<=0 and len(pq)==0:
            answer[0]=cur_time
            break
        call()
        
    return answer"""



#기존 heapq보다 1/5로 실행시간 단축(pop대신 인덱스를 활용)
"""import heapq

def solution(program):
    answer = [0]*11
    program.sort(key=lambda x : x[1])
    #print(program)
    pos=0
    n=len(program)
    cur_time=0
    pq=[]
    exe=0
    #print(pos,n)
    def call():
        nonlocal pos
        while pos<n and cur_time>=program[pos][1]:
            heapq.heappush(pq,program[pos])
            pos+=1
    while len(pq)>0 or pos<n:
        if len(pq)==0:
            cur_time=program[pos][1]
            call()
        exe=heapq.heappop(pq)
        answer[exe[0]]+=cur_time-exe[1]
        cur_time+=exe[2]
        #print(exe,answer,cur_time)
        call()
    answer[0]=cur_time
        
    return answer"""