from collections import defaultdict
def solution(today, terms, privacies):
    answer = []
    day=[]
    name=[]
    dic=defaultdict(int)
    for i in terms:
        t,e=i.split()
        dic[t]=int(e)
    #print("terms=",dic)
    Y,M,D=map(int,today.split("."))
    
    for i in privacies:
        a,b=i.split()
        day.append(a)
        name.append(b)
    #print(day,name)
    for i in range(len(day)):
        y,m,d=map(int,day[i].split("."))
        m+=int(dic[name[i]])
    
        if m>12:
            y+=m//12
            m=m%12
            if m==0:
                y-=1
                m=12
            #print(i+1,y,m,d)
        
        if Y>y :
            answer.append(i+1)
        elif Y==y and M>m:
            answer.append(i+1)
        elif Y==y and M==m and D>=d:
            answer.append(i+1)
        else:
            continue
        #print(answer)
    
    return answer