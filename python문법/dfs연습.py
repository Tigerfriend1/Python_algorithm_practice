#중복순열
#nHk
#L은 k와 비교 후 탈출하는 변수
#p는 배열
def DFS(n,k,L,p):
    if L==k:
        for x in p:
            print(x)
    else :
        for i in range(1,n+1):
            p.append(i)
            DFS(n,k,L+1,p)
            p.pop()

def solution(n,k):
    DFS(n,k,0,[])

print(solution(3,2))