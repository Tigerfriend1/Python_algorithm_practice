from collections import deque
def solution(prices):
    answer = []
    dq=deque(prices)
    #chk=[0]*len(prices)
    #print(answer)
    
    while dq:
        now_prices=dq.popleft()
        flag=0
        cnt=0
        for i,val in enumerate(dq):
            if flag==1:
                break
            elif flag==0 and now_prices<=val: #증가 혹은 같음.
                cnt+=1
            else:
                cnt+=1
                flag=1
        answer.append(cnt)
                    
    return answer

#다시 풀기. 직관적으로 표현.
"""from collections import deque
def solution(prices):
    answer = []
    dq=deque(prices)
    
    while dq:
        cnt=0
        now=dq.popleft()
        for i in dq:
            if now>i:
                cnt+=1
                break
            else:
                cnt+=1
        answer.append(cnt)
    
    
    return answer"""