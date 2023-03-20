import math
def solution(n):
    answer = 0
    numList=[0]*(n+1)
    def serch(i):
        if i==0 or i==1:
            return False
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                return False
        return True
    for i in range(len(numList)):
        if serch(i):
            answer+=1
            
    return answer