s=input("enter ").split( )
even=[]
odd=[]
for i in s:
    i=int(i)
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print(even)
print(odd)