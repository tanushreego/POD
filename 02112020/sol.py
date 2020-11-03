print ("solution1")
n=int(input())
m=int(input())
a=m+2
b=n-(m+a)

while (b>a and m+a+b==n):
    print(m,a,b)
    a=a+2
    b=n-m+a