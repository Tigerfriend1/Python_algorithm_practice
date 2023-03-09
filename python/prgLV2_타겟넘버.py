def solution(numbers, target):
    answer = 0
    mynum=0
    case=[1,-1]
    nowlist=[]
    def DFS(nowlist,mynum,numbers):
        #print(nowlist)
        nonlocal answer
        if len(numbers)==0 and mynum==target:
            answer+=1
            return
        #print('a')
        for i in case:
            if len(numbers)!=0:
                a=numbers[0]
                nowlist.append(a*i)
                DFS(nowlist,mynum+a*i,numbers[1:])
                nowlist.pop()
                
    DFS(nowlist,mynum,numbers)
    
    return answer


print(solution([4, 1, 2, 1],4))

#deque를 활용해 pop과 append의 속도를 O(1)로 만들어 속도를 줄인다. 실제로 최대 941ms의 속도를 840ms로 줄어들었다.
"""from collections import deque
def solution(numbers, target):
    answer = 0
    case=[1,-1]
    mysum=0
    mylist=[]
    dq=deque(numbers)
    def DFS(dq,mysum,mylist):
        nonlocal answer
        
        if len(dq)==0 and mysum==target:
            answer+=1
            return
            #print(mysum, answer, mylist)
        for i in case:
            if len(dq)!=0:
                num=dq.popleft()
                mylist.append(num)
                DFS(dq,mysum+num*i,mylist)
                dq.appendleft(num)
                mylist.pop()
    DFS(dq,mysum,mylist)
        
    
    return answer"""