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


"""from collections import deque
def solution(prices):
    answer = [0]*len(prices)
    stack=deque()
    stack.append(0)
    for i in range(1,len(prices)):
        if prices[i]<prices[stack[-1]]:
            for j in stack.reverse():
                if prices[i]<prices[j]:
                    answer[j]=i-j
                    stack.remove(j)
                else:
                    break
        stack.append(i)
        
    
    return answer"""