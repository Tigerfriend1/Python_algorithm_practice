def solution(n):
    answer = []
    
    
    def DFS(s1,s2,s3,n):
        if n==1:
            answer.append([s1,s3])
            return
        DFS(s1,s3,s2,n-1) #가장 큰 원반을 남기고 두번째 칸으로 이동
        answer.append([s1,s3]) #가장 큰 원반을 3번째로 옮김
        DFS(s2,s1,s3,n-1) #남은 원반을 2번째에서 3번째로 옮김
        
            
            
    DFS(1,2,3,n)
        
    
    return answer