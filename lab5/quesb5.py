N = int(input("Enter a number: "))

if N < 0:
    print("Invalid! Factorial not possible.")
else:
    fact = 1
    i = 1
    while i <= N:
        fact = fact * i
        i = i + 1
    print("Factorial =", fact)