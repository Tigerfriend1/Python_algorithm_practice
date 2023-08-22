import sys
input=sys.stdin.readline

K,N=map(int,input().split())

List=[]
for i in range(K):
    List.append(int(input().rstrip()))


List.sort()

answer=0
start=1
end=List[-1]
def binary(start,end):
    global answer
    if start>end:
        return answer
    mid=(start+end)//2
    num=0
    for i in List:
        num+=i//mid
    if num>=N:# 한번 같아서 값을 저장하더라도 여기를 탈출할때까지는 길이가 커지기 때문에 답을 업데이트한다.
        answer=mid
        start=mid+1
        binary(start,end)
    elif num<N:
        end=mid-1
        binary(start,end)
    
binary(start,end)
print(answer)
    






