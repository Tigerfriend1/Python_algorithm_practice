import math
def solution(brown, yellow):
    answer = []
    
    for i in range(1,int(math.sqrt((brown+yellow)))+1):
        y=brown/2+2-i
        if i*y==brown+yellow:
            answer=[y,i]
            break
    return answer