def solution(s, n):
    answer = ''
    #print(ord('a'),ord('z'),ord('A'),ord('Z'))
    #print(chr(97))
    a=0
    for i in s:
        if i==" ":
            answer+=i
            continue
        if 97<=ord(i)<=122: 
            if ord(i)+n>122:
                a=ord(i)+n-(122-97)-1 #26
            else:
                a=ord(i)+n
        elif 65<=ord(i)<=90:
            if ord(i)+n>90:
                a=ord(i)+n-(90-65)-1 #26
            else:
                a=ord(i)+n
        answer+=chr(a)
    return answer