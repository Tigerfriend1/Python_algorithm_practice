def solution(command):
    answer = [0]*2 #x,y
    R=0
    L=0 #R,L의 횟수를 체크
    R_L=(R-L)%4
    case=[0,1,2,3]
    
    for i in command:
        if i=="G":
            if case[R_L]==0:
                answer[1]+=1
            elif case[R_L]==1:
                answer[0]+=1
            elif case[R_L]==2:
                answer[1]-=1
            else :
                answer[0]-=1
        elif i=="B":
            if case[R_L]==0:
                answer[1]-=1
            elif case[R_L]==1:
                answer[0]-=1
            elif case[R_L]==2:
                answer[1]+=1
            else:
                answer[0]+=1
            
        elif i=="R":
            R+=1
        else: #i=="L"
            L+=1
        R_L=(R-L)%4
        #print(answer,R,L)
            
    
    return answer
print(solution("GRGLGRG"))


#풀이 길이를 줄인 방식
"""def solution(command):
    answer = [0,0]
    dxy=[[0,1],[1,0],[0,-1],[-1,0]]
    d=0
    for i in command:
        if i=="G":
            answer[0]=answer[0]+dxy[d][0]
            answer[1]=answer[1]+dxy[d][1]
        elif i=="B":
            answer[0]=answer[0]-dxy[d][0]
            answer[1]=answer[1]-dxy[d][1]
        elif i=="R":
            d+=1
            d=d%4
        else:
            d-=1
            d=d%4
            
    return answer"""