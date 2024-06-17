# import numpy as np
# a=list(map(int,input().split()))
# arr=np.array(a).reshape(2,3)

r=2
c=2

a=[]
for i in range(0,4):
    sub=[]
    print("Enter the values for row",i)
    for j in range(0,c):
        print("Enter the values for column",j)
        ele=int(input())
        sub.append(ele)
        print(sub)
    a.append(sub)
    print(a)
    
d={}
ans=[]
for i in range(0,r):
    for j in range(0,c):
        if a[i][j] not in d:
            d[a[i][j]]=1
        else:
            d[a[i][j]]+=1
            if d[a[i][j]]==2:
                ans.append(a[i][j])
print(d)

#missing
for i in range(1,r**2+1):
    if i not in d:
        ans.append(i)
print(d)
print(ans)


