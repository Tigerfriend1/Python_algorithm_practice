answer = -1
#k=현재 피로도 / d= 던전돈 횟수
def DFS(k,d,dungeons): 
    global answer
    if len(dungeons)==0:
        answer = max(answer,d)
        #print('answer=',answer)
        return
        
    for i,dungeon in enumerate(dungeons):
        if k>=dungeon[0] : #현재 피로도가 입장조건보다 크거나 같을때 입장
            #print(k,d,dungeons)
            dungeons.remove(dungeon)
            DFS(k-dungeon[1],d+1,dungeons)
            dungeons.insert(i,dungeon)
            """d-=1
            k+=dungeon[1]"""
            
            #print('new=',k,d,dungeons)
            
        else: #더이상 던전을 돌 수 없는 상황(깊이를 다 들어간것)
            answer = max(answer,d)
            #print('answer=',answer)

        
    

def solution(k, dungeons):
    DFS(k,0,dungeons)
    global answer
    
    
    return answer

