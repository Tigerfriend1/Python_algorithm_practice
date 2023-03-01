from itertools import permutations
import math
def solution(numbers):
    answer = 0
    List=set()
    for i in range(len(numbers)):
        a=list(permutations(numbers,i+1))
        #print(a)
        for j in a:
            List.add(int(''.join(j)))
            #print(List)
    
    def serch(i):
        if i==0 or i==1:
            return False
        for j in range(2,int(math.sqrt(i))+1):
            if i%j==0:
                return False
        #print('i=',i)
        return True
            
    
    for i in List:
        if serch(i):
            answer+=1
        
            
        
    
    return answer