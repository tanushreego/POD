n1=input().split(" ")
d=[]
for i in range(int(n1[1])):
    inp=input().split(" ")
    d.append(inp)
for i in range(len(d)):
    for j in range(len(d[i])):
        d[i][j]=int(d[i][j])
def Sort(d): 
    d.sort(key = lambda x: x[0]) 
    return d 
Sort(d)  
count=0
for i in d:
    if int(n1[0])>int(i[0]):
        n1[0]=int(i[1])+int(n1[0])
        count+=1
if count==int(n1[1]):
    print("YES")
else:
    print("NO")
