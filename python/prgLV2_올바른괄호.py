def solution(s):
    answer = True
    
    # [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
    #print('Hello Python')
    chk1=0
    
    for i in s:
        if chk1==0 and i==')':
            return False
        elif chk1!=0 and i==')':
            chk1-=1
        else:
            chk1+=1
    if chk1!=0:
        return False
    
    return True