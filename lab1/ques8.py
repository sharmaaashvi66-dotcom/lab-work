s=int(input("enter no of sec"))
if s<1 or s>86400:
    print("invalid input")
else:
    h=s//3600
    h1=s%3600
    m=h1//60
    sec=h1%60
    print(h,":",m,":",sec)