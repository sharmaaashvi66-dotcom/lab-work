n = int(input())
d = {}
for i in range(n):
    country, capital = input().split()
    d[country] = capital
name = input()
if name in d:
    print(d[name])
else:
    print("Not found")