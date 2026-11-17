c=0
s=input().split()
for i in s:
    i=int(i)
    if i==0:
        c+=1
        s.pop(i)
for j in range(c):
    l=[]
    l.append(0)
se=s+l
print(se)