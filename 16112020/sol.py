import operator
from collections import Counter
n = int(input())
students = []
score={}
for i in range(n):
    inp = input().split(" ")
    sc={inp[0] : int(inp[1])*10 + int(inp[2])*30 + int(inp[3])*50}
    score.update(sc)
cd = sorted(score.items(),key=operator.itemgetter(1),reverse=True)
rank = 1
score_count=[]
for i in cd:
    score_count.append(i[1])

score_count=dict(Counter(score_count))
student_rank={}
temp={}
temp1=cd[0][1]
init=0

for i in cd:

    if temp1!=i[1]:
        if init!=0:
            rank=rank+score_count[temp1]
    student_rank.update({i[0]:rank})
    temp1=i[1]
    init=1

for i in student_rank:
    print(student_rank[i]," ",i)