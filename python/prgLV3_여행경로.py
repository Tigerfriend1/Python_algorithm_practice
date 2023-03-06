import copy
answer = ["ZZZ"]
def solution(tickets):
    global answer
    ways=['a']
    next_city=0
    
    def DFS(tickets,way,next_city):
        global answer
        if len(tickets)==0:
            
            #print(way)
            #print(next_city)
            for i in range(len(way)):
                if answer[i]<way[i]:
                    break
                elif answer[i]>way[i]:
                    
                    answer=way.copy()
                    #print('?',answer,next_city)
                    answer.append(next_city)
                    return
                else:
                    pass
            return
        
        if way[0]=='a':
            print("start")
            way.pop()
            for i,val in enumerate(tickets):
                if val[0]=='ICN':
                    next_city=val[1]
                    
                    del tickets[i]
                    way.append(val[0])
                    DFS(tickets,way,next_city)
                    way.pop()
                    tickets.insert(i,val)
                    
        else:
            for i,val in enumerate(tickets):
                if val[0]==next_city:
                    next_city=val[1]
                    
                    
                    del tickets[i]
                    way.append(val[0])
                    
                    DFS(tickets,way,next_city)
                    way.pop()
                    tickets.insert(i,val)
                    
                        
    DFS(tickets,ways,next_city)    
    
    
    
    return answer