from collections import defaultdict

def solution(gems):
    answer = [0,0]
    lt=0
    maxL=100000
    a = len(set(gems)) #보석 종류수
    sh = defaultdict(int)
    for rt in range(len(gems)) : 
        sh[gems[rt]]+=1
        
        
        while len(sh)==a:
            if maxL>rt-lt+1: #모든종류보석을 사는걸 만족한 상태에서, 길이가 더 작은걸 채택
                answer=[lt+1,rt+1]
                maxL=rt-lt+1
        
            sh[gems[lt]]-=1
            if sh[gems[lt]] ==0:
                del sh[gems[lt]]
            lt+=1
            
                    

    return answer