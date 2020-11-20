n=input()
lists=[n[i:j] for i in range(len(n)) for j in range(i+1,len(n)+1)]
vol=['a','e','i','o','u']
lists1=[]
for i in lists:
    if i not in lists1:
        lists1.append(i)
c=0
for i in lists1:
    for j in vol:
        if j in i:
            c+=1

print(lists)
print("number of sweet allowed: ",c)