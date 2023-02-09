from collections import deque
from collections import defaultdict

def BFS(s,e):
    dq=deque()
    dq.append(s) #출발점
    check=defaultdict(int)
    check[s]+=1
    L=0
    while (dq):
        len_dq=len(dq)
        for _ in range(len_dq):
            v=dq.popleft()
            for nv in [v-1,v+1,v+5]:
                if check[nv]==0:
                    check[nv]=+1
                    dq.append(nv)
                if nv==e:
                     return L+1
        L+=1
    
    
        

def solution(s, e):
    answer = BFS(s, e)
    return answer