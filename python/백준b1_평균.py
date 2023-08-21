import sys
input=sys.stdin.readline

N=int(input())

List=[]

List=list(map(int,input().split()))
List.sort(key = lambda x : -x)

big = List[0]
for i in range(N):
    List[i]=(List[i]/big)*100
print(sum(List)/N)

# 9
# 10 20 30 40 50 60 70 80 90
# 답 : 55.55555555555556