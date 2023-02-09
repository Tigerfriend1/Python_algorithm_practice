cnt=0
def DFS(a,visited,graph): #v=간선 2번째 간선을 기준으로 첫번째를 끊는다.
    global cnt
    visited[a]=1
    cnt+=1
    
    for i in graph[a]: #a=4 [3,5,6,7]
        if visited[i]==0:
            DFS(i,visited,graph)
    return cnt
    

def solution(n, wires):
    global cnt
    answer = 1000
    graph=[[]for _ in range(len(wires)+2)]
    print(graph)
    for a,b in wires:
        graph[a].append(b)
        graph[b].append(a)
    print(graph)
    minL=100
    for a,b in wires:
        visited=[0]*101
        visited[b]=1
        cnt=0
        DFS(a,visited,graph)
        
        minL = min(abs(cnt-(n-cnt)),minL)
        
    answer=minL
        
    
    
    
    
    return answer

print(solution(7,[[1,2],[2,7],[3,7],[3,4],[4,5],[6,7]]))