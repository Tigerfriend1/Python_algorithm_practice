def solution(word):
    answer = 0
    case=['A','E','I','O','U']
    myword=''
    flag=0
    def DFS(myword): #DFS의 그 다음걸 붙임
        nonlocal answer, flag
        
        if flag==1:
            return
        if myword==word:
            flag=1
            return answer
        answer+=1
        if len(myword)==5:
            return
        for alpa in case:
            DFS(myword+alpa)
            
    DFS(myword) 
        
    return answer