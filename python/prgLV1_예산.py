from collections import deque
def solution(d, budget):
    answer = 0
    d.sort()
    #print(d)
    dq=deque(d)
    now=dq.popleft()
    while now<=budget:
        budget-=now
        answer+=1
        if len(dq)!=0:
            now=dq.popleft()
        else:
            break
    return answer