n=int(input("enter your number"))
if n>=1000 and n<=9999:
    a=n//100
    b=n%100
    c=a//10+a%10
    d=b//10+b%10
    if a==b:
        print("equal")
    else:
        print("non equal")