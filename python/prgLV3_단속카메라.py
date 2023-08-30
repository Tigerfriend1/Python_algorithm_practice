def solution(routes):
    answer = 0
    routes.sort(key=lambda x : x[1])
    #print(routes)
    pre=-30001
    for a,b in routes:
        #print(a,b)
        
        if pre<a: #pre 15
            pre=b
            answer+=1
        #print(pre)
        
    return answer