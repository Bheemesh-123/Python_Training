# def fel(n):
#     if n<=1:
#         return 1
#     else:
#         return (fel(n-1)+7*fel(n-2)+n//4)%(10**9+7)
# num=8
# print(fel(num))

n=int(input())
x=[1,1]
for i in range(2,n+1):
    ans=(x[i-1]+7*x[i-2]+i//4)%(10**9+7)
    x.append(ans)
print(x[n])