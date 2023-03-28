N=int(input())

# 3,5
a=0
# if N>15:
#     a+=N//15
#     b=N%15
if N>=5 and (N%5)%3==0:
    a+=N//5
    a+=(N//5)//3
    print(a)
elif N%3==0:
    a+=N//3
    print(a)
else:
    print(-1)
    
