n=input("enter")
c=0
s=0
d=0
sc=0
for i in n:
    for j in n[i]:
        if n[i][j].capital():
            c+=1
        elif n[i][j].lower():
            s+=1
        elif n[i][j].digits():
            d+=1
        else:
            sc+=1