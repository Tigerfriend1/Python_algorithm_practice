from collections import defaultdict

def solution(input_string):
    answer = ''
    dic=defaultdict(int)
    chk=defaultdict(int)
    for i, val in enumerate(input_string):
        if i>=1 and input_string[i-1]!=input_string[i]: #값이 이미 한번 나온 알파벳
            dic[input_string[i-1]]=10000        #다음에 나오면 걸러내기 위한 10000값
        if chk[val]==0 and dic[val]>=10000:     #chk는 값이 여러번 answer에 저장되는걸 막기위함.
            answer+=val
            chk[val]=1 
        dic[val]+=1
    
    if len(answer)==0:
        answer='N'
    answer=list(answer)
    answer.sort()
    a=''
    for i in answer:
        a+=i
    return a