s=input()
i=0
c=0
while i<len(s)-1:
    if s[i]=="0" and s[i+1]=="0":
        c+=1
        i+=2
    else:
        c+=1
        i+=1
if i<len(s):
    c+=1
print(c)