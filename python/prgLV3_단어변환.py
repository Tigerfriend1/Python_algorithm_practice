from collections import defaultdict
def solution(begin, target, words):
    answer = 51
    cnt=0
    chk=defaultdict(int)
    
    def DFS(nowWord):
        nonlocal cnt,chk,answer
        if nowWord==target:
            answer=min(answer,cnt)
            
        for word in words:
            wordChk=0
            for j,val in enumerate(word):
                if nowWord[j]!=word[j]:
                    wordChk+=1
            if chk[word]==0 and wordChk==1:
                cnt+=1
                chk[word]+=1
                
                DFS(word)
                chk[word]-=1
                cnt-=1
                
            
    if target not in words:
        answer=0
    DFS(begin)
    if answer==51:
        answer=0
    return answer