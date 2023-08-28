# 0 1 2 3 0 1 2 3 반복(인덱스 반복 활용)
a=0
#a+=1
for i in range(10):
    a=(a+1)%4
    print(a)

b=[]
#2차원배열 초기화
for _ in range(8):
    b.append([0]*8)
b[0][0]=1
print(b)

if 2 not in b:
    print("A")

a = 1 if 5>1 else 0
#-> 한줄로 줄인것
d=[1,2,3,4,5,6]
c=[n*2 for n in d if n!=2]
print(c)