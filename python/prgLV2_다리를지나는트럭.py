from collections import deque
def solution(bl, w, tw):
    Bl=deque([0]*bl)
    dq=deque(tw)
    time=0
    total=0
    cur_w=0
    while dq:
        time+=1
        total-=Bl[0]
        Bl.popleft()
        if w<total+dq[0]:
            Bl.append(0)
        else:
            Bl.append(dq[0])
            total+=dq.popleft()
        #print(time,Bl,dq)
        
    return time+bl