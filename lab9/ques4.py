lar=0
s=input("enter").split()
small=s[len(s)-1]
small=int(small)
for i in s:
    i=int(i)
    if i>lar:
        lar=i
    elif i<small:
        small=i
print(lar)
print(small)