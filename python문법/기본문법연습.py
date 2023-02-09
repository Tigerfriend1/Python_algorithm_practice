a=2
print(type(a))
print(type(str(a)))
print(type(a))
b=str(a)
print('b is ', type(b))
print('b is ',type(b),'holy~~')

if (1>3 and 1<3 or 1) :
    print(a)
else :
    print('b is ',type(b),'holy~~')

if(-2):
    print("-2 is exist!")
if(0) : 
    print('?')
else : 
    print('0 is not exist')

if (b):
    print("oh")

if('c'in'cat') : 
    print("c in cat!!")

if('c'not in'dog'):
    print('c not in dog')


print(bool('c'in'cat'))
print('c'in'cat')


lang = "python"
print(lang[-1])
print(lang[-3:6])
print(lang[::1])

#list : 대괄호로 정의 슬라이싱 가능 // len사용가능 // in 사용가능 // .append(값) : 뒤에 값을 붙임
#튜플 : 소괄호로 정의, 단, 수정이 불가함. 읽기 전용 리스트
#set : 중괄호로 정의, a.intersection(b) : 교집합 출력 / a.union(b) : 합집합, 중복안됨 / a.difference(b) : 차집합
#딕셔너리 : 중괄호로 정의 dic = {key1 : value1, key2 : value2...} key값이 인덱스 역할을 함. /출력은 dic[key1]
#딕2 : .get(key3)를 하면 에러가 나지 않고, None이 출력됨 /dic[key3]=value3는 값 추가
vv={'a','b'}
vv.add

for i in range(3):
    print ("go")

for i in range(1,10,2):
    print (i)

print('----------------------')
dic = {1:'a', 2:'b', 3:'c', 4:'d'}

for k in dic.keys():
    print(k)

print('----------------------')

for v in dic.values():
    print(v)

print('----------------------')
for k,v in dic.items():
    print(v,k)

while 1 :
    print(dic)
    break

#List comprehension : new_list=[x for x in my_list if x==3] -> my_list안에 3이 있는지를 파악할 수 있다.
my_list = ['H']
#print(my_list.lower())  #리스트는 lower이 안됨. str로 뽑은 이후 lower메소드를 적용할 수 있음.
new_list = [p.lower() for p in my_list ]
print(new_list)

def my_fuc(a,b):
    c=a+b
    return c,b
print(*my_fuc(1,2))

def your_fuc(a,b,c=1):
    d=a+b+c
    print(f'a={a}, b={b}, c={c}, d={d}')
    return d
print(f"so, d is {your_fuc(2,4)}")

def our_fuc(a=1,b=1,c=1,d=1,e=1,f=1):
    g=a+b+c+d+e+f
    return g
print (our_fuc(e=5))

TK="good"
def tk_fuc():
    global TK   #함수 안에서 전역변수를 사용하기 위함.
    TK="gg"
    print(TK)
tk_fuc()
print(TK)

#-----------------------------------------
#input을 통해 입력 받기 가능

'''my_input=input()

print(my_input)
my_list_input=list(my_input)
print(my_list_input)'''

#----------------------------------------
#class // 딕셔너리는 변수를 다루는 용이고, 클래스는 여기에 기능(함수를 넣을 수 있다.)
class BlackBox:
    pass
b1 = BlackBox() # 객체 생성 // c++과 다르게 객체 생성이 BlackBox b1이 아니다.
b1.name='Inavi'
print(isinstance(b1,BlackBox))
print(b1.name) #이거는 임의로 내가 변수를 만들어 준거임.

class BigBox:
    def __init__(self, name, price) :
        self.name = name
        self.price = price
    def set_travel_mode(self):
        print('여행모드 on')
        

B1=BigBox('tk',20)
print(B1.name,B1.price)
B1.set_travel_mode()

class TravelBigBox(BigBox):
    def __init__(self, name, price, sd):
        super().__init__(name, price) #super를 통해 상속된걸 수정가능
        self.sd=sd

    def set_joy_mode(self):
        print('Have a joy~')

B2=TravelBigBox('jj', 30, '64g')
print(B2.name,B2.price)
B2.set_travel_mode()
B2.set_joy_mode()

try:
    pass
except:
    pass
else:
    pass
finally:
    pass

print('시험시작------')
t='10203'
p='15'
def solution(t, p):
    answer = 0
    
    for a in range(len(t)-len(p)) :
        print(a)
        new_t=t[a:a+len(p)]
        print(f'new_t is {new_t}')
        
        if int(new_t)<=int(p):
            answer+=1
            print(new_t)
            

    
    return answer

print(solution(t,p))
print('---------')
print(int('02'))
print(lang.replace[-1])