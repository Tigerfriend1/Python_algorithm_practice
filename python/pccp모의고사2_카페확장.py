from collections import deque

def solution(menu, order, k):
    answer = 0
    dq=deque()
    idx=0
    comple=-1
    for i in range(k*(len(order)-1)+1):
        if comple==i: #완료(즉, 사람을 먼저 보내고 손님이 입장해야함.)
            dq.popleft()
            comple=-1
        if i%k==0: #k초당 사람 추가
            dq.append(order[idx])
            idx+=1
        if comple==-1 and len(dq)>0: #작업할 여유가 있는지 확인.
            comple=i+menu[dq[0]] #완료시간은 현재시간부터 커피제작시간 더해줘야함.
        answer=max(answer,len(dq))    
    return answer

print(solution([5, 12, 30], [1, 2, 0, 1], 10))