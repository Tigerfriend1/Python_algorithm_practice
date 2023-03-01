def solution(sizes):
    answer = 0
    maxa=0
    maxb=0
    sum=0
    sum2=0
    for a,b in sizes:
        """maxa=max(maxa,a)
        maxb=max(maxb,b)"""
        sum=max(maxa,a)*max(maxb,b)
        sum2=max(maxa,b)*max(maxb,a)
        if sum>=sum2:
            answer=sum2
            maxa=max(maxa,b)
            maxb=max(maxb,a)
        else:
            answer=sum
            maxa=max(maxa,a)
            maxb=max(maxb,b)
        
        #print(sum,sum2,answer)
    return answer