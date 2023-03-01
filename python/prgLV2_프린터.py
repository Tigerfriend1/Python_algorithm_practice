from collections import deque

def solution(priorities, location):
    answer = 0
    len_p=len(priorities)
    List=[]
    for i,val in enumerate(priorities):
        List.append([val,i])
    
    dq=deque(List)
    maxq=sorted(priorities, reverse=True)
    
    cnt=0
    while dq:
        doc=dq.popleft() #2,0
        if maxq[0]!=doc[0]:
            dq.append(doc)
            continue
        if doc[1]==location:
            return cnt+1
        cnt+=1
        del maxq[0]
        