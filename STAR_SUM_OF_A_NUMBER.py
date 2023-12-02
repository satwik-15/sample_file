T=int(input())
while(T!=0):
    N=int(input())
    a=0
    for j in range(N):
        n=j
        while(n!=0):
            n=n//10
            a=a+n
        s=a+j
    c=0
    for i in range(N+1):
        if s>i:
            c=c+1
    print(c)
   