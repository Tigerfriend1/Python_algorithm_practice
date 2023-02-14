#배열사용능력 확인
from collections import defaultdict
import math
def solution(fees, records):
    answer=[]
    intime=[0]*10000
    isin=[0]*10000
    sumT=[0]*10000
    for i in records:
        a,b,c=i.split()
        time=a.split(':')
        new_time=int(time[0])*60+int(time[1])
        if len(c)==2:
            intime[int(b)]=new_time
            
            isin[int(b)]=1
        else :
            sumT[int(b)]+=new_time-intime[int(b)]
            isin[int(b)]=0
    for i,val in enumerate(isin):
        if val == 1:
            sumT[i]+=(23*60+59)-intime[i]
    
    x1 = int(fees[0])
    x2 = int(fees[1])
    x3 = int(fees[2])
    x4 = int(fees[3])
    for i,val in enumerate(sumT):
        if val != 0:
            if val<=x1:
                answer.append(x2)
            
            else :
                answer.append(x2+math.ceil((val-x1)/x3)*x4)
            
            
    
    return answer