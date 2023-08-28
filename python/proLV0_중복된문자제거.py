#pccp연습문제

from collections import defaultdict
def solution(my_string):
    dic=defaultdict(int)
    for i in my_string:
        dic[i]+=1
    print(dic)
    answer=dic.keys()
    print(answer)
    answer = ''.join(list(answer))
    return answer
