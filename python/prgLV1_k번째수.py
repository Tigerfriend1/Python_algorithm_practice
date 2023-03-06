def solution(array, commands):
    answer = []
    narray=[]
    for i,j,k in commands:
        narray=array[i-1:j]
        narray.sort()
        answer.append(narray[k-1])
        #print(answer)
    
    return answer
print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))