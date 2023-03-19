import math
def solution(dr):
    answer = 0
    prego=1
    nowgo=1
    preNum=0
    nowNum=0
    flag=0
    for i in range(len(dr)):
        q=dr[i]
        
        if dr[i]=="1" and dr[i+1]=="0"and flag==0:
            flag=1
            #print("ff")
            continue
        if flag==1:
            q=10
            flag=0
            #print("뭐가문제야",q)
        try:
            int(q)
            #print("gogo",q,prego,preNum)
            if i!=0:
                
                answer+=prego*preNum
                preNum=nowNum
                prego=nowgo
                #print("answer",answer)
            nowNum=int(q)
            #print("NN",nowNum,q)
            nowgo=1
        except:
            if q=="*" and preNum==0:
                nowgo=nowgo*2
            elif q=="*" and preNum!=0:
                nowgo=nowgo*2
                prego=prego*2
            elif q=="S":
                nowNum=nowNum
            elif q=="D":
                nowNum=nowNum*nowNum
            elif q=="T":
                nowNum=nowNum*nowNum*nowNum
            elif q=="#":
                nowgo=-nowgo
        #print(prego, nowgo, preNum, nowNum)
    #print(prego, nowgo, preNum, nowNum)
    answer+=prego*preNum+nowgo*nowNum
    #print("answer=",answer)
            
    return answer