# To reverse the given number and square it and print the values of each digit 
n=int(input())
def sod(n):
    c=0
    while n>0:
        c=c+1
        n=n//10
    return c
# print(sod(n))    //To print the digit of input number
def rev(n):
    ans=0
    while n>0:
        digit=n%10
        sq=digit**2
        sod_sq=sod(sq)
        ans=ans*(10**sod_sq)+sq
        n=n//10
    return ans
ans=rev(n)
def rev2(n):
    ans2=0
    while n>0:
        digit=n%10
        ans2=ans2*10 + digit
        n=n//10
    return ans2
print(rev2(ans))
