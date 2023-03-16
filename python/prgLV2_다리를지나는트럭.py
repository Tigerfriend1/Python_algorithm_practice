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

#다시 풀기
"""from collections import deque
def solution(bridge_length, weight, truck_weights):
    dq=deque(truck_weights) #대기트럭
    nowb=deque([0]*bridge_length) #다리를 건너는 트럭
    nowW=0
    cnt=0
    while len(dq)!=0:
        a=nowb.popleft()
        nowW-=a
        now=dq.popleft()
        if nowW+now>weight:
            nowb.append(0)
            dq.appendleft(now)
        else:
            nowb.append(now)
            nowW+=now
        
        cnt+=1
        #print(nowb,nowW,now)
    
    return cnt+bridge_length"""