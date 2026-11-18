n = int(input("enter"))
d = {}
for i in range(n):
    country, capital = input().split()
    d[country] = capital
name = input("enter")
if name in d:
    print(d[name])
else:
    print("Not found")