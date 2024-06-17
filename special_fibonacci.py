#Recursion function
# def sfib(n):
#     if n<=1:
#         return 1
#     else:
#         return (sfib(n-1)*sfib(n-1)+(n-2)*(n-2))%(47)
# num=int(input())
# print(sfib(num))

#interation method

n=int(input())
x=[1,1]
for i in range(2,n+1):
    ans=(x[i-1]*x[i-1]+(i-2)*(i-2))%47
    x.append(ans)
print(x[n])