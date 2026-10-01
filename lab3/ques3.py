a1=int(input("enter"))
a2=int(input("enter"))
a3=int(input("enter"))
if a1+a2+a3==180:
    if a1==90 or a2==90 or a3==90:
        print("right angled triangle")
    elif a1>90 or a2>90 or a3>90:
        print("obtuse angled triangle")
    else:
        print("acute angled triangle")
        