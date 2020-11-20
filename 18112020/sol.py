n=input()
def rot(num):
    lst=[]
    if num[0]=="9":
        lst=[9]
        for i in range(1,len(num)):
            x=9-int(num[i])
            lst.append(x)
    else:
        for i in range(len(num)):
            x=9-int(num[i])
            lst.append(x)
    return lst
st=(rot(n))
def convert(list1): 
    s = [str(i) for i in list1] 
    res = int("".join(s)) 
      
    return(res) 
print(convert(st)) 

