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
        


#보다 직관적인 풀이
"""from collections import deque
def solution(priorities, location):
    new=[]
    for i,val in enumerate(priorities):
        new.append((i,val))
    dq=deque(new)
    cnt=0
    while dq:
        flag=0
        now=dq.popleft()
        for i in range(len(dq)):
            if dq[i][1]>now[1]:
                dq.append(now)
                flag=1
                break
        if flag==1:
            continue
        elif flag==0 and now[0]==location:
            return cnt+1
        else:
            cnt+=1"""