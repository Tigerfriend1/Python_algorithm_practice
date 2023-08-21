import sys

input = sys.stdin.readline
List = []
N = int(input())

for i in range(N):
    List.append(input().rstrip())


List=list(set(List))
List.sort(key=lambda x: (len(x), x))
for i in List:
    print(i)

# 13
# but
# i
# wont
# hesitate
# no
# more
# no
# more
# it
# cannot
# wait
# im
# yours