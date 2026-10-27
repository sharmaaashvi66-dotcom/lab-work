n = int(input("enter n= "))
div = 0
notdiv = 0
x = int(input("enter x= "))
while x != -999:
    if x % n == 0:
        div = div + 1
    else:
        notdiv = notdiv + 1
    x = int(input("enter x= "))
print (div)
print (notdiv)
