a=list(map(int,input().split()))
mp=-999
ans=0
for i in range(1,len(a)-1):
    if a[i]>a[i-1] and a[i]>a[i+1]:
        p=a[i]
        if p>mp:
            mp=p
            ans=i
print(ans)