a = [int(x) for x in input("Enter integers: ").split()]
n = len(a)

for i in range(n):
    for j in range(0, n - i - 1):
        if a[j] < a[j + 1]:
            temp = a[j]
            a[j] = a[j + 1]
            a[j + 1] = temp

print("Descending order:", a)