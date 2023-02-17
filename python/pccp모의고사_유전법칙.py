from collections import deque

rs=0
def back(n,p): #부모세대를 추적해나감. (3,5)->3,4라고하자. 
    global rs
    case=['RR','Rr','Rr','rr']
    if n>1:
        par_n=n-1
        par_p=p//4
        back(par_n,par_p)
    #1,0
    if n==1:
        rs='Rr'
    elif rs=='Rr':
        rs=case[p%4]
    elif rs=='RR':
        rs=='RR'
    elif rs=='rr':
        rs=='rr'
    
    

        
            

def solution(queries):
    answer = []
    
    for i in queries:
        a,b=i
        print(a,b)
        back(a,b-1)
        print(rs)
        answer.append(rs)
        
        
        
    
    return answer