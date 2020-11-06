print ("solution1")
n=int(input())
m=int(input())
a=m+2
b=n-(m+a)
while(b>a and m+a+b==n):
    m1=m
    a1=a
    b1=b
    while ( b1 > a1 and m1 + a1 + b1 == n ) :
        print (m1 , a1 , b1 )
        a1 = a1 + 2
        b1=n-(m1+a1)
m+=2
a=m+2
b=n-(m+a)