n1=int(input("enter"))
n=n1
d=0
while n>0:
    r=n%10
    d=(d*10)+r
    n=n//10
if d==n1:
    print("palindrome")
else:
    print("not a palindrome")