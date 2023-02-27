from collections import defaultdict
def solution(nums):
    answer = 0
    len_n=len(nums)
    sh=defaultdict(int)
    for i in nums:
        sh[i]+=1
    print(sh)
    answer=min(len(sh),len_n/2)
    
    return answer