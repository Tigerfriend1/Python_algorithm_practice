def solution(ingr):
    answer = 0
    
    stack=[]
    for i in ingr:
        stack.append(i)
        #print(stack[-4:])
        if stack[-4:]==[1,2,3,1]:
            for j in range(4):
                stack.pop()
            answer+=1
            
    
        
        
    return answer