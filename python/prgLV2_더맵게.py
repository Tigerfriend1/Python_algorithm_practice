import heapq
def solution(scoville, K):
    answer = 0
    sco=[]
    for i in scoville:
        heapq.heappush(sco,i)
    #print(sco)
    cnt=0
    chk=0
    while sco[0]<K:
        a=heapq.heappop(sco)
        b=heapq.heappop(sco)
        heapq.heappush(sco,a+b*2)
        cnt+=1
        if len(sco)<=2:
            for i in sco:
                chk+=i
            if chk<K:
                return -1
        #print(a)
    return cnt