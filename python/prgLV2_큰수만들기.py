def solution(number, k):
    answer = ''
    stack=[]
    
    for i in number:
        if len(stack)==0:
            stack.append(i)
            continue
        if stack[-1]<i:
            while(k and len(stack)!=0):
                if stack[-1]>=i:
                    break
                stack.pop()
                k-=1
        stack.append(i)
        #print(stack)
    if k!=0:
        while k:
            stack.pop()
            k-=1
    answer=''.join(stack)
    #print(k)
        
    
    return answer