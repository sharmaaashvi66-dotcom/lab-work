w = input()
d = {}
for i in w:
    if i in d:
        d[i] = d[i] + 1
    else:
        d[i] = 1
print(d)