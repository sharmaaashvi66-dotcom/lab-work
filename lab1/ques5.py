x=int(input("enter"))
y=int(input("enter"))
if x<0 or y<0:
    print("invalid input")
else:
    if y%x==0:
        print("divisible")
    else:
        print("not divisible")