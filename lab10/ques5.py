def simple_interest(p, r, t=1):
    si = (p * r * t) / 100
    return si
p = float(input("enter"))
r = float(input("enter"))
print("1 year:", simple_interest(p, r))
print("3 years:", simple_interest(p, r, 3))