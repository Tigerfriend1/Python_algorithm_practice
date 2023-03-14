from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    dq=deque(people)
    #print(people)
    while(dq):
        if len(dq)==1:
            dq.pop()
            answer+=1
            break
        elif dq[0]+dq[-1]>limit:
            dq.pop()
            answer+=1
        else:
            dq.popleft()
            dq.pop()
            answer+=1
    
    return answer