# To print the 
n=input()
v="aeiou"
d={}
mx=-999
for i in n:
    if i in v:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
        if d[i]>mx:
            mx=d[i]
            ans=i
print(d)
print(ans)


    # To print the first character of vowel present in the input string      
# n=input()
# v="aeiou"
# d={}
# for i in n:
#     if i in v:
#         print(i)
#         break