def process(n):
    mx=-999
    c=0
    ans=0
    while n>0:
        digit=n%10
        if digit>mx:
            mx=digit
        c=c+1
        n=n//10
    #arrange
    while c>0:
        ans=ans*10 + mx
        c=c-1
        
        
        
        
n=list(map(int,input().split()))
for i in n:
    ans=
    f_ans+=ans