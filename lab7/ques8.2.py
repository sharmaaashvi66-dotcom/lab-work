a = [int(x) for x in input("Enter integers: ").split()]
product = 1

for i in range(len(a)):
    product *= a[i]

print("Product:", product)