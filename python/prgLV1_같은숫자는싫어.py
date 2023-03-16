def solution(arr):
    answer = []
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')
    pre=-1
    for i,val in enumerate(arr):
        if pre!=val:
            answer.append(val)
        pre=val
    #print(answer)
    
    return answer

#stack으로 풀기

"""def solution(arr):
    answer = []
    arr.reverse()
    pre=-1
    now=-1
    for i in range(len(arr)):
        now=arr.pop()
        if now!=pre:
            answer.append(now)
        pre=now
    
    return answer"""

#훨씬 간편한 stack으로 풀기

"""def solution(arr):
    stack=[arr[0]]

    for i in range(1,len(arr)):
        if stack[-1]!=arr[i]:
            stack.append(arr[i])
        
    return stack"""