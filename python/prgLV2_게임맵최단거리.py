from collections import deque
def solution(maps):
    answer = 0
    dq=deque()
    dq.append([0,0])
    while len(dq)>0:
        x,y=dq.popleft()
        #print(x,y)
        for dx,dy in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx,ny=x+dx,y+dy
            if nx<0 or ny<0 or nx>=len(maps) or ny>=len(maps[0]) or maps[nx][ny]==0 :
                continue
            if maps[nx][ny]==1:
                maps[nx][ny]=maps[x][y]+1
                dq.append([nx,ny])
            
            
        
    answer=maps[len(maps)-1][len(maps[0])-1]
    if answer==1:
        answer=-1
    
    return answer

print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))