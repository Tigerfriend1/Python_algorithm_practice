def solution(s):
    answer = 0
    cnt1=0
    cnt2=0
    a=[]
    b=""
    flag=0
    for i in range(len(s)):
        if len(b)==0:
            x=s[i]
        if x==s[i]:
            cnt1+=1
            b+=(s[i])
        elif x!=s[i]:
            cnt2+=1
            b+=(s[i])
        #print(b,cnt1,cnt2)
        if cnt1==cnt2!=0:
            cnt1==0
            cnt2==0
            #answer+=1
            a.append(b)
            b=""
    #print(a)
    if len(b)!=0:
        answer=len(a)+1
    else:
        answer=len(a)
    return answer