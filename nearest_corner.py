s=list(input().split())
chair=input()
#find index
z=999
c_ind=s.index(chair)

#till c_ind
for i in range(0,c_ind):
    if s[i]=="-":
        if abs(c_ind-i)-1<z:
            z=abs(c_ind-i)-1
#right side
for i in range(c_ind+1,len(s)):
    if s[i]=="-":
        if abs(i-c_ind)-1<z:
            z=abs(i-c_ind)-1
            
print(z)
            