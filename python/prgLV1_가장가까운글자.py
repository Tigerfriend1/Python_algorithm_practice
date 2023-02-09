"""def countLetters(word):
    counter = {}
    for letter in word:
        if letter not in counter:
            counter[letter] = 0
        counter[letter] += 1
    return counter

print(countLetters('banana'))"""

"""from collections import defaultdict

def countLetters(word):
    counter = defaultdict(lambda:0)
    for letter in word:
        counter[letter]+=1
    return counter

print(countLetters('banana'))"""

from collections import defaultdict
k=2
id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["ryan con", "ryan con", "ryan con", "ryan con","muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
report = list(set(report))
report_list = defaultdict(set)
report_count = defaultdict(int)
    
for i in report:
    a,b = i.split()
    report_list[a].add(b)
    report_count[b]+=1
#리스트에는 누가 누구를 신고했는지 담았고, 카운터에는 신고누적횟수가 담김
answer=[]
for name in id_list:
    mail_count = 0
    for user in report_list[name]:
        if report_count[user]>=k:
            mail_count+=1
    answer.append(mail_count)

print(answer)