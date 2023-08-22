import math
import sys
input=sys.stdin.readline
N=int(input())

N=list(str(math.factorial(N)))

#print(N)
cnt=0
for i in N[::-1]:
    #print(i)
    if i!='0':
        break
    else:
        cnt+=1

print(cnt)