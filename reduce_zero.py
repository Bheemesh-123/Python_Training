x=int(input())
y=int(input())
T=0
while y>0:
    if x<y:
        x,y=y,x
    T=x-y
    x=y
    y=T
print(x)