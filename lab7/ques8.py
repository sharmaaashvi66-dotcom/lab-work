a = [int(x) for x in input("Enter integers: ").split()]
total = 0

for i in range(len(a)):
    total += a[i]

print("Sum:", total)