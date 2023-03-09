#queue로 풀기 list보다 시간효율적임.
from collections import deque
def solution(phone_book):
    answer = True
    cchk=0
    phone_book.sort()  
    dq=deque(phone_book)
    nowValue=dq.popleft()
    while dq:
        compValue=dq.popleft()
        for i in range(len(nowValue)): #nowValue길이만큼만 비교    
            if nowValue[i]!=compValue[i]:
                cchk=1
                break
        if cchk==0:
            return False
        nowValue=compValue
        cchk=0
        
                
    return answer

#list로 풀기
"""def solution(phone_book):
    answer = True
    cchk=0
    phone_book.sort()   
    for a in range(1, len(phone_book)):
        nowValue=phone_book[a]
        preValue=phone_book[a-1]
        for i in range(len(preValue)): #nowValue길이만큼만 비교    
            if nowValue[i]!=preValue[i]:
                cchk=1
                break
        if cchk==0:
            return False
        cchk=0
        
                
    return answer"""

print(solution(["119", "97674223", "1195524421"]))