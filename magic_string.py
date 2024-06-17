s=input()
d={}
mx=-999
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
    if d[i]>mx:
        mx=d[i]
print(len(s)-mx)
        