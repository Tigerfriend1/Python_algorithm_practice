def solution(n):
    answer = ''
    case=[1,2,4]
    case2=[1,2,4]
    
    a=n//3
    b=n%3
    while n>0:
        n-=1
        a=n//3
        b=n%3
        answer=str(case2[b])+answer
        n=a
        print(answer,n)
    
    
    return answer
