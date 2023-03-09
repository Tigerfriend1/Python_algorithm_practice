#union-find방식의 풀이
def solution(n, computers):
    answer = 0
    parent=[x for x in range(n)]
    print(parent)
    graph =[[] for _ in range(len(computers))]
    
    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if computers[i][j]==1:
                graph[i].append(j)
    print(graph)
    
    def Find(node):
        if parent[node]==node:
            return node
        parent[node]=Find(parent[node])
        return parent[node]
            
    def Union(i,j):
        if Find(i)!=Find(j):
            parent[Find(i)]=parent[Find(j)]
            
    for i in range(len(graph)): #[0,1] i는 컴퓨터이름
        for j in graph[i]:  #0 , 1 j는 i랑연결된 컴퓨터 이름
            Union(i,j)
    
    for i in range(len(parent)):
        Find(i)
    
    print('p=',parent)
    sh=set(parent)
    print(sh)
    answer=len(sh)
                
    return answer

#DFS로 풀이 : 보다 쉽게 구현 가능
"""def solution(n, computers):
    answer = 0
    chk=[0]*n
    cnt=0
    graph=[[] for _ in range(n)]
    for i in range(n):
        for j in range(len(computers[i])):
            if i==j:
                continue
            if computers[i][j]==1:
                graph[i].append(j)
    def DFS(point):
        nonlocal cnt,answer
        for i in point:
            if chk[i]==0:
                chk[i]=1
                DFS(graph[i])
        
    groupNum=0
    for i,point in enumerate(graph):
        if chk[i]==0:
            chk[i]=1
            DFS(point)
            #여기서 나왔다는건 한줄을 끝까지 이었다는 것.
            groupNum+=1
    answer=groupNum
        
    return answer"""