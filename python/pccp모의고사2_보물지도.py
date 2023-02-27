from collections import deque
def solution(n, m, hole):
    answer = 0
    borad=[[0 for _ in range(m+1)] for _ in range(n+1)]
    dist=[[[-1,-1] for _ in range(m+1)] for _ in range(n+1)]
    for x,y in hole:
        borad[x][y]=1
    dq=deque()
    dq.append([1,1,0])
    dist[1][1][0]=0
    while len(dq)>0:
        x,y,cs=dq.popleft()
        for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            for s in range(2):
                if cs==1 and s==1:
                    continue
                nx,ny,ns=x+dx*(s+1),y+dy*(s+1),cs|s
                if nx<1 or ny<1 or nx>n or ny>m or borad[nx][ny]>0 or dist[nx][ny][ns]!=-1:
                    continue
                dq.append([nx,ny,ns])
                dist[nx][ny][ns]=dist[x][y][cs]+1
    answer=dist[n][m][1]
                
                
    return answer