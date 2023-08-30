from collections import defaultdict
def solution(keymap, targets):
    answer = []
    dic=defaultdict(int)
    #각 키에 접근하려면 몇번을 눌러야하는지를 저장
    for i in keymap:
        for j,alpa in enumerate(i):
            if dic[alpa] and dic[alpa]>j+1: #더 적게 눌러서 가능하면
                dic[alpa]=j+1
            elif dic[alpa] and dic[alpa]<j+1:
                continue
            else:
                dic[alpa]=j+1
    print(dic)            
    for i in targets:
        cnt=0
        for j in i:
            if j not in dic:
                cnt=-1
                break
            cnt+=dic[j]
        answer.append(cnt)
    return answer