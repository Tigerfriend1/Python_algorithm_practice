def solution(numbers, target):
    answer = 0
    mynum=0
    case=[1,-1]
    nowlist=[]
    def DFS(nowlist,mynum,numbers):
        print(nowlist)
        nonlocal answer
        if len(numbers)==0 and mynum==target:
            answer+=1
            #print(nowlist)
            
            return
        #print(numbers)
        #for num in numbers:
        print('a')
        for i in case:
            if len(numbers)!=0:
                a=numbers[0]
                nowlist.append(a*i)
                DFS(nowlist,mynum+a*i,numbers[1:])
                nowlist.pop()
    DFS(nowlist,mynum,numbers)
    
    return answer


print(solution([4, 1, 2, 1],4))