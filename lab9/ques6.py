menu=input().split()
price=input().split()
o=input()
for i in range(len(menu)):
    if o==menu[i]:
        c=i
        break
print(o,"X 1 =",int(price[c]))