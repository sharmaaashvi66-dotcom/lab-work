n = tuple(map(int, input().split()))
even = ()
for i in n:
    if i % 2 == 0:
        even = even + (i,)
print(even)