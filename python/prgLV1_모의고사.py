from collections import defaultdict

def solution(answers):
    answer = []
    a=[(x%5)+1 for x in range(10000)]
    b=[2,1,2,3,2,4,2,5]*1250
    c=[3,3,1,1,2,2,4,4,5,5]*10000
    count=defaultdict(int)
    for i,val in enumerate(answers):
        if val==a[i]:
            count[1]+=1
        if val==b[i]:
            count[2]+=1
        if val==c[i]:
            count[3]+=1
    answer=[k for k,v in count.items() if max(count.values())==v]
    answer.sort()   
    return answer