sum=0
s=input().split()
l=[]
for i in s:
    if i in ['0','1','2','3','4','5','6','7','8','9']:
        i=int(i)
        l.append(i)
print(l)
for j in l:
    j=int(j)
    sum+=j
print(sum)