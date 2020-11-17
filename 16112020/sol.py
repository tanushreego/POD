import operator
n = int(input())
students = []
score={}
for i in range(n):
    inp = input().split(" ")
    sc={inp[0] : int(inp[1])*10 + int(inp[2])*30 + int(inp[3])*50}
    score.update(sc)
    cd = sorted(score.items(),key=operator.itemgetter(1),reverse=True)
    students.append(inp)
print (students)
print(cd)