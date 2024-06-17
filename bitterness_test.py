a=list(map(int,input().split()))
b=list(map(int,input().split()))
mini=999
for i in range(len(a)):
    if a[i]+b[i]<mini:
        mini=a[i]+b[i]
print(mini)