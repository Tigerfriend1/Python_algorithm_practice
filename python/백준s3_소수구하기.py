import sys
input = sys.stdin.readline

N,M=map(int,input().split())

board=[i for i in range(N,M+1)]

print(board)
len_b=len(board)
for i in range(len_b):
    for j in range(i,len_b):
        if board[j]/board[i]==0:
