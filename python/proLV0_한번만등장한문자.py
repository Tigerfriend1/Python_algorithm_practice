from collections import defaultdict
def solution(s):
    answer = ''
    dic = defaultdict(int)
    for i in s:
        dic[i]+=1
    for i in dic.items():
        if i[1]==1:
            answer+=i[0]
    return ''.join(sorted(answer))