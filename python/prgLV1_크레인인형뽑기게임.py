from collections import deque
def solution(board, moves):
    answer = 0
    space=[]
    dq=deque(moves)
    while dq:
        nowTurn=dq.popleft()
        for i in range(len(board)):
            if board[i][nowTurn-1]!=0:
                if len(space)!=0 and space[-1]==board[i][nowTurn-1]:
                    space.pop()
                    board[i][nowTurn-1]=0
                    answer+=2
                    break
                space.append(board[i][nowTurn-1])
                board[i][nowTurn-1]=0
                break
        
        #print(space)
    
    return answer