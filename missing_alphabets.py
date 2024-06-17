str=input()
s="abcdefghijklmnopqrstuvwxyz"
s1=""
for i in s:
    if i not in str:
        s1+=i
print(s1)