string=input()
def rot(st):
    r1=st[0:len(st)-1]
    r2=st[len(st)-1:len(st)]
    r=r2+r1
    print(r)
    return r
lists=[string]
get =string
for i in range(len(string)):
    get=rot(get)
    if get not in lists:
        lists.append(get)
print(len(lists))