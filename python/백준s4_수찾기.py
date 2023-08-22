import sys
input=sys.stdin.readline

N=int(input())

List1=list(map(int,input().split()))

M=int(input())
List2=list(map(int,input().split()))


List1.sort()

# print(List1)
# print(List2)

answer=0
def myfind(List,num,start,end):
    global answer
    if start>end: #탈출문(없다는 뜻)
        return False
    mid=(start+end)//2
    
    if num>List[mid]:
        myfind(List,num,mid+1,end)
    elif num==List[mid]:
        answer=1
    elif num<List[mid]:
        myfind(List,num,start,mid-1)
    else:
        return False    
        

for i in List2:
    myfind(List1,i,0,N-1)
    print(answer)
    answer=0
    

# 5
# 4 1 5 2 3
# 5
# 2 3 7 9 5