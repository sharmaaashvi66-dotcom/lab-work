s=input().split()
lar=s[len(s)-1]
for i in s:
    if len(i)>len(lar):
        lar=i
print(lar)