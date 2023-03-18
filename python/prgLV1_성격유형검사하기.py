from collections import defaultdict
def solution(survey, choices):
    answer = ''
    case=[3,2,1,0,1,2,3]
    dic=defaultdict(int)
    for i,val in enumerate(survey):
        if choices[i]==4:
            pass
        elif choices[i]<4:
            dic[survey[i][0]]+=case[choices[i]-1]
        elif choices[i]>4:
            dic[survey[i][1]]+=case[choices[i]-1]
        
    #print(dic)
    
    if dic["R"]>=dic["T"]:
        answer+="R"
    elif dic["R"]<dic["T"]:
        answer+="T"
        
    if dic["C"]>=dic["F"]:
        answer+="C"
    else:
        answer+="F"
    if dic["J"]>=dic["M"]:
        answer+="J"
    else:
        answer+="M"
    if dic["A"]>=dic["N"]:
        answer+="A"
    else:
        answer+="N"
    return answer