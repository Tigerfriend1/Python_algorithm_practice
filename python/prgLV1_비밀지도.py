def solution(n, arr1, arr2):
    answer = [[] for _ in range(n)]
    map1=[]
    map2=[]
    for i in range(n):
        if len(format(arr1[i],'b'))<n:
            a=(n-len(format(arr1[i],'b')))*'0'+str(format(arr1[i],'b'))
            
        else :
            a=str(format(arr1[i],'b'))
        if len(format(arr2[i],'b'))<n:
            b=(n-len(format(arr2[i],'b')))*'0'+str(format(arr2[i],'b'))
        else :
            b=str(format(arr2[i],'b'))
        for j in range(n):
            if a[j]==b[j]=='0':
                answer[i]+=" "
            else:
                answer[i]+="#"
        answer[i]=''.join(answer[i])
         
    

    return answer