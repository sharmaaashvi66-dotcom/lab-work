wicket=0
boundary=0
runs=0
s=input("enter").split()
for i in s:
    if i=="W":
        wicket+=1
    elif i=="4" or i=="6":
        boundary+=1
for j in s:
    if j=="W":
        continue
    else:
        j=int(j)
        runs+=j
print(wicket)
print(boundary)
print(runs)
