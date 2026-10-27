N = int(input("Enter how many terms: "))

a, b = 1, 1   
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
