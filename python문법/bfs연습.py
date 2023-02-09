from collections import deque

def BFS():
    dq=deque()
    dq.append(1)
    L=0
    while dq:
        dq_len=len(dq)
        for _ in range(dq_len): #dq길이만큼 돌면서 왼쪽에선 출력+삭제 / 오른쪽에선 다음값 추가
            v=dq.popleft()
            print(v,end=' ')
            for nv in [v*2,v*2+1]:
                if nv>7:
                    continue
                dq.append(nv)
        L+=1
    return

BFS()



