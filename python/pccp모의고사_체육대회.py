from collections import defaultdict
maxL=0
def DFS(L,s,ability,chk): #L은 과목현재횟수, s는 현재능력값
    global maxL
    n=len(ability)
    m=len(ability[0])
    if L==m:
        maxL=max(maxL,s)
    else:
        for i in range(n):  #학생수 만큼 돈다.
            if chk[i]==0:
                chk[i]=1
                DFS(L+1,s+ability[i][L],ability,chk)
                chk[i]=0
                
            
        
                
    

def solution(ability):
    answer = 0
    #print(ability)
    
    chk=[0]*11
    DFS(0,0,ability,chk)
    answer=maxL
    
        
    
    return answer