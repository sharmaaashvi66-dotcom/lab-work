import math
x1=float(input("enter x1"))
y1=float(input("enter y1"))
r=float(input("enter r"))
x2=float(input("enter x2"))
y2=float(input("enter y2"))
d=math.sqrt(((x2-x1)**2)+((y2-y1)**2))
if d<r:
    print("inside the boundary")
elif d==r:
    print("on the boundary")
else:
    print("outside the boundary")
