x=int(input("enter x"))
y=int(input("enter y"))
n=int(input("enter n"))
for i in range(x+1,y+1):
    if i%n==0:
        print(i,end=" ")
print()