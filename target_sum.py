# from numpy import sort
# n=list(map(int,input().split()))
# num=int(input())
# so=sort(n)
# print((so))
# j=0
# for i in range(0,len(so)):
#     if so[i]+so[j+1]==num:
#         print(i,j+1)
#     else:
#         j=j+1

a=list(map(int,input().split()))
t=int(input())
a.sort()
i=0
j=len(a)-1
ans=0
while i<j:
    curr_sum=a[i]+a[j]
    if curr_sum==t:
        print(i,j)
        i+=1
        j-=1
    elif curr_sum<t:
        i+=1
    else:
        j-=1