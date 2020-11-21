num=int(input())
lists=[]
for i in range(num):
    n=int(input())
    lists.append(n)
lists.sort()
sum2=0
if len(lists)==1:
    sum2=int(lists[0])
else:
    while len(lists)>1: 
        sum1=int(lists[0])+int(lists[1])
        sum2=sum2+sum1
        lists.append(sum1)
        lists.remove(lists[0])
        lists.remove(lists[0])
        lists.sort()
print(sum2)