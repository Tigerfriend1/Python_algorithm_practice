

from copy import deepcopy
def solution(board):
    answer = 0
    dy=[0,0,1,0,-1,1,-1,1,-1]
    dx=[0,1,0,-1,0,1,-1,-1,1]
    b=deepcopy(board)
    len_b=len(board)
    #board[i][j]
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 1:
                for k in range(9):
                    ny=i+dy[k]
                    nx=j+dx[k]
                    if 0<=ny<len_b and 0<=nx<len_b:
                        b[ny][nx]=1
            else :
                continue
    print(b)
    for i in b:
        for j in i:
            if j==0:
                answer+=1
    return answer
board = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]
solution(board)