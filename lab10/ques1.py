l=input().split()
v=int(input("enter"))
t=tuple(l)
for i in t:
    i=int(i)
print(t)
print(len(t))
print(t.count(v))
print(t.index(v))