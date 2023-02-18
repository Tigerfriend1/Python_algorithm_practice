import heapq
def solution(ability, number):
    hq=[]
    answer=0
    for i in range(len(ability)):
        heapq.heappush(hq,ability[i])
    for i in range(number):
        a=heapq.heappop(hq)
        b=heapq.heappop(hq)
        heapq.heappush(hq,a+b)
        heapq.heappush(hq,a+b)
        #print(hq,a,b,number)
    answer=sum(hq)
        
    return answer