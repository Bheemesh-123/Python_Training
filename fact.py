def fact(n):
    if n==0:
        return 1
    else:
        return n*fact(n-1)  
nu=int(input("Enter NUm:"))
print(fact(nu))
