from collections import defaultdict

def solution(array):
    dic = defaultdict(int)
    for i in array:
        dic[i] += 1
    
    dicc = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    print(dicc)
    if len(dicc) > 1 and dicc[0][1] == dicc[1][1]:  # 빈도가 같은 최빈값이 있을 경우
        return -1
    else:
        return dicc[0][0]
