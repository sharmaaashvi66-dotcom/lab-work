n=int(input("enter"))
for i in range(n//2):
    if n%i==0:
        print("not prime")
    else:
        print("prime")
        