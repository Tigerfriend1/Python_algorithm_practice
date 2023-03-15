def solution(numbers, hand):
    answer = ''
    pad=[[1,2,3],[4,5,6],[7,8,9],[-1,0,-2]]
    caseL=[1,4,7]
    caseR=[3,6,9]
    nowL=[3,0]
    nowR=[3,2]
    for i in numbers:
        if i in caseL:
            answer+='L'
            nowL=[caseL.index(i),0]
        elif i in caseR:
            answer+='R'
            nowR=[caseR.index(i),2]
        else:
            nowPos=[0,0]
            
            for j in range(4):
                if i in pad[j]:
                    nowPos=[j,pad[j].index(i)]
                    break
            dl=abs(nowL[0]-nowPos[0])+abs(nowL[1]-nowPos[1])
            dr=abs(nowR[0]-nowPos[0])+abs(nowR[1]-nowPos[1])
            if dl<dr:
                answer+='L'
                nowL=nowPos
            elif dr<dl:
                answer+='R'
                nowR=nowPos
            else:
                if hand=='left':
                    answer+='L'
                    nowL=nowPos
                else:
                    answer+='R'
                    nowR=nowPos
        #print(answer)
    
    return answer
