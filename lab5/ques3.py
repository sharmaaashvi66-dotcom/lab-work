c=0
d=0
n=int(input("enter num"))
i=int(input("enter i"))
while i!=-999:
    if i%n==0:
        d+=1
    else:
        c+=1
    i=int(input("enter i"))
print("divisible",d)
print("not divisible",c)