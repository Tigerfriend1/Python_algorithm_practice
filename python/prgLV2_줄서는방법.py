import math
def solution(n, k):
    answer = []
    num=[i for i in range(1,n+1)]
    k=k-1
    #인덱스는 0번부터 시작하기때문에 맞춰줌.
    while num:
        a=math.factorial(n-1)
        idx=k//a
        answer.append(num[idx])
        del num[idx]
        k=k%a
        n-=1
    return answer