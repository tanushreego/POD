num=int(input())
lists=[]
for i in range(num):
    n=int(input())
    lists.append(n)
lists.sort()
print(lists)
sum1=int(lists[0])
lis=[]
if len(lists)==1:
    lis.append(sum1)
else:
    for i in range(1,len(lists)):
        sum1=sum1+int(lists[i])
        lis.append(sum1)
s=0
for i in lis:
    s=s+int(i)
print(s)



