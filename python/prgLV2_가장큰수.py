#문제해결 포인트 : sort()의 조건을 스스로 만들 수 있는가.
from functools import cmp_to_key
def solution(numbers):
    answer = ''
    List=[]
    for i in numbers:
        List.append(str(i))
    #List=list(set(List))

    def compare(a,b):
        temp1=a+b
        temp2=b+a
        if temp1>temp2:
            return 1
        elif temp1<temp2:
            return -1
        else:
            return 0
    
    List.sort(key=cmp_to_key(compare),reverse=True)
    answer=''.join(List)
    if int(answer)==0:
        answer='0'
    
    return answer