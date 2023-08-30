from collections import defaultdict

def solution(name, yearning, photo):
    answer = []
    dic=defaultdict(int)
    for i,val in enumerate(name):
        dic[val]=yearning[i]
    for i in photo:
        score=0
        for j in i:
            if dic[j]:
                score+=dic[j]
            else:
                continue
        answer.append(score)
    
    return answer