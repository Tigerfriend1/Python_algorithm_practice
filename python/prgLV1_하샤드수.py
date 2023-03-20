def solution(x):
    answer = True
    a=str(x)
    asum=0
    for i in range(len(a)):
        asum+=int(a[i])
        #print(asum,a[i])
    if x%asum!=0:
        return False
    return answer