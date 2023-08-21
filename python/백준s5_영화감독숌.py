import sys
input=sys.stdin.readline

N=int(input())

init=666

while N!=0:
    if '666'in str(init):
        N-=1
        if N==0:
            break
    init+=1

print(init)

#187 -> 66666
#500 -> 166699