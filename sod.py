# Sum of digits using Recursion

def sod(n):
    if n==0:
        return 0
    else:
        return n%10 + sod(n//10)
num=int(input())
res=sod(num)
print("The sum of digits of number is ",res) 