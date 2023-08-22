from collections import deque
import sys
input = sys.stdin.readline

N=int(input())
List = []
for i in range(N):
    List.append(int(input().rstrip()))


dq=deque(List)
answer=''
now=dq.popleft()
stack=[]
for i in range(1,N+1):
    stack.append(i)
    answer+='+'
    while stack and stack[-1]==now:
        stack.pop()
        answer+='-'
        if dq:
            now=dq.popleft()
    
if len(stack)!=0: #정상 종료하면 stack이 비어있어야함. stack에 남아있다면 수열을 만들 수 없다는 것.
    print('NO')
else:
    for i in answer:
        print(i)
