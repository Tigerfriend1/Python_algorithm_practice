from collections import defaultdict
def solution(s):
    answer = 0
    result=""
    word=""
    dic=defaultdict()
    dic[0]="zero"
    dic[1]="one"
    dic[2]="two"
    dic[3]="three"
    dic[4]="four"
    dic[5]="five"
    dic[6]="six"
    dic[7]="seven"
    dic[8]="eight"
    dic[9]="nine"
    dic={v:k for k,v in dic.items()}
    #print("dic=",dic)
    #print(dic["three"])
    for i in s:
        #print(i)
        try :
            int(i)
            result+=str(i)
            #print(i)
        except:
            #print("Ex :",i)
            word+=i
        if word in dic:
            result+=str(dic[word])
            word=""
    if len(word)!=0:
        result+=str(dic[word])
    #print("ans=",result)
            
    answer=int(result)
    return answer