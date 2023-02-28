from collections import defaultdict
def solution(participant, completion):
    answer = ''
    sh=defaultdict(int)
    for i in participant:
        sh[i]+=1
    #print(sh)
    for i in completion:
        sh[i]-=1
    for i in sh:
        #print(sh[i])
        if sh[i]==1:
            answer=i
            break
    #print(sh)
    
    return answer



#better answer
"""from collections import Counter

def solution(participant, completion):
    answer = ''
    answer=list(Counter(participant)-Counter(completion))
    #print(sh)
    
    return answer[0]"""