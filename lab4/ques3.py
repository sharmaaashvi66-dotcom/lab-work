shape=input("enter type of square")
if shape=="square":
    s=int(input("enter side"))
    a=s**2
elif shape=="rectangle":
    l=int(input("enter lenght"))
    b=int(input("enter breadth"))
elif shape=="circle":
    r=int(input("enter radius"))
    a=3.14*r**2
elif shape=="triangle":
    b=int(input("enter base"))
    h=int(input("enter height"))
    a=0.5*b*h
else:
    print("invalid iput")
print(a)