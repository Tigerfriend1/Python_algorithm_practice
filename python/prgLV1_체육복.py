import copy
def solution(n, lost, reserve):
    answer = 0
    lostt=lost.copy()
    for i in lostt:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
    for i in range(1,n+1):
        if i in lost:
            if i-1 in reserve:
                reserve.remove(i-1)
                lost.remove(i)
                answer+=1
                continue
            elif i+1 in reserve:
                reserve.remove(i+1)
                lost.remove(i)
                answer+=1
                continue
            else:
                continue
        answer+=1
    return answer
print(solution(13, [1, 2, 5, 6, 10, 12, 13], [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]))


#다른 풀이
"""def solution(n, lost, reserve):
    answer=0
    st=[1]*(n+1)
    #print(st)
    for i in lost:
        st[i]-=1
    for i in reserve:
        st[i]+=1
    #print(st)
    for i in range(1,n+1):
        if st[i]==0:
            if i>1 and st[i-1]==2:
                st[i]+=1
                st[i-1]-=1
            elif i!=n and st[i+1]==2:
                st[i]+=1
                st[i+1]-=1
        #print(st)
    for i in range(1,n+1):
        if st[i]>0:
            answer+=1
    return answer"""