n=int(input())
a=list(map(int,input().split()))
p_max=-999
k=0
h=0
for i in range(1,len(a)):
    for j in range(i+1,len(a)):
        if a[i]+a[j]==18:
            if a[i]>a[j]:
                p=a[i]*a[j]
                if p>p_max:
                    p_max=p
                    k=a[i]
                    h=a[j]
print(p_max,k,h)
            
        