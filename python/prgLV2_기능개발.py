import math
def solution(progresses, speeds):
    answer = []
    before=-1
    relese=0
    for i,val in enumerate(progresses):
        if relese==0:
            before=math.ceil((100-val)/speeds[i])
            relese+=1
            
        elif relese>=1 and before >= math.ceil((100-val)/speeds[i]):
            relese+=1
        else : #relese는 있고, 뒤에 과정이 완료가 더 남았을때
            answer.append(relese)
            relese=1
            before=math.ceil((100-val)/speeds[i])
        if i==len(progresses)-1:
            answer.append(relese)
        #print(i+1,before,relese,answer)
        
    return answer


#stack사용(deque로 stack구현)
"""import math
from collections import deque
def solution(progresses, speeds):
    answer = []
    dq=deque(progresses)
    dqs=deque(speeds)
    #print(dq)
    relese=0
    before=0
    while dq:
        now=dq.popleft()
        nows=dqs.popleft()
        if relese==0:
            before=math.ceil((100-now)/nows)
            relese=1
        elif relese!=0 and before>=math.ceil((100-now)/nows):
            relese+=1
        else:
            answer.append(relese)
            relese=1
            before=math.ceil((100-now)/nows)
        if len(dq)==0 and relese!=0:
            answer.append(relese)
    
    return answer"""