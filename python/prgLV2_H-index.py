def solution(citations):
    answer = 0
    citations.sort()
    cnt=0
    #print(citations)
    len_c=len(citations)
    for i in range(len_c):
        
        if (len_c - i)>=citations[i]:
            answer=citations[i]
            cnt=0
            #print(answer)
        else :
            cnt+=1
    #현재까지의 h값과 그 값보다 큰값들의 개수를 비교하여 큰 값을 최대 h값으로 선정        
    if cnt>answer:
        answer=cnt
    
    return answer