#union-find
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
        for j in graph[i]:#0 , 1 j는 i랑연결된 컴퓨터 이름
            Union(i,j)
    
    
    for i in range(len(parent)):
        Find(i)
    
    print('p=',parent)
    sh=set(parent)
    print(sh)
    answer=len(sh)
                
    
    return answer