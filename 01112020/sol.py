n=input("enter even no. of digits: ")
l=len(n)
if l%2==0:
    n1=[]
    n2=[]
    for i in range(0,l,2):
        n1.append(n[i])
        n2.append(n[i+1])
    def listsum(l1):
        s=0
        for i in l1:
            s=s+int(i)
        return s
    s1=listsum(n1)
    s2=listsum(n2)
    print("sum 1: ",s1)
    print("sum 2: ",s2)
    diff=s2-s1
    print("difference is: ",diff)
else:
    print("please input even digits number")
        
        
        
