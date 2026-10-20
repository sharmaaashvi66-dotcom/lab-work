n= int(input("Enter your number: "))
i=0
while i<1000:
    i+=1
    if i%n==0:
        continue
    print(i)