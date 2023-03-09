from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    Map=[[-1 for _ in range(102)] for _ in range(102)]
    for rect in rectangle: #rect=1,1,7,4
        x1,y1,x2,y2 = map(lambda x : x*2,rect)
        for i in range(x1,x2+1):
            for j in range(y1,y2+1):
                if x1<i<x2 and y1<j<y2:
                    Map[i][j]=0
                elif Map[i][j]!=0:
                    Map[i][j]=1
    dq=deque()
    dq.append([characterX*2, characterY*2])
    visited=[[1]*102 for _ in range(102)]
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    while dq:
        x,y=dq.popleft()
        if x==itemX*2 and y==itemY*2:
            answer=visited[x][y]//2
            break
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if Map[nx][ny]==1 and visited[nx][ny]==1:
                dq.append([nx,ny])
                visited[nx][ny]=visited[x][y]+1
        
    #print(rectangle)
    #print(Map)
    
    return answer