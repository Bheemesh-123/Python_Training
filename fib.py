def fib(n):
    if n<=1:
        return n
    if n==2:
        return 1
    return fib(n-1)+fib(n-2)
nt=int(input("Enter the num:"))
for i in range(nt):
    print(fib(i))