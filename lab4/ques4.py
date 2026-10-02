h=int(input("enter hour"))
m=int(input("enter minute"))
m+=15
if h<=23:
    if m>=60:
        if h==23:
            h=00
        else:
            h+=1
        m=m%60
        m1=m//10
        m2=m%10
        print("enter time",h,":",m1,m2)
else:
    print("invalid input")