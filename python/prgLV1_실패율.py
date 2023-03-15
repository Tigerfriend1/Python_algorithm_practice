def solution(N, stages):
    answer = []
    challCnt=[0]*(N+2)
    players=len(stages)
    for i in stages:
        challCnt[i]+=1
    #print(challCnt)
    for i in range(1, N+1):
        if players==0:
            failRate=0
        else:
            failRate=challCnt[i]/players
            players-=challCnt[i]
        answer.append((i,failRate))
    #print(answer)
    answer.sort(key=lambda x : (-x[1],x[0]))
    answer=[x[0] for x in answer]
    
    return answer
        