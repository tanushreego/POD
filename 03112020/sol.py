num=int(input())
def checkprime(n):
    primelist=[2]
    for j in range(3,n):
        
        c=0
        for i in range(2,j):
            if j%i==0:
                c+=1
        if c==0:
            primelist.append(j)
    return primelist
prime=[]
prime=checkprime(num)
s=0
count=0
for i in prime:
    s=s+i
    if s==num:
        count+=1
        break
if count!=0:
    print("yes")
else:
    print("no")
