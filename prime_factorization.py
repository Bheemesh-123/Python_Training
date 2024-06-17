def pf(n):
    ans=[]
    i=2
    while i<=n:
        if n%i==0:
            ans.append(i)
            n=n//i
        else:
            i=i+1
    return ans
ans=pf(6)
s=0
a=[11,21,32,45,1,23]  # a=list(map(int,input().split()))
for i in ans:
    s+=a[i]
print(s)
