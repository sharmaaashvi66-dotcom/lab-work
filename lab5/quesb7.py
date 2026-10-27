
n = int(input("Enter a number: "))

if n <= 0:
    print("Invalid input")
else:
    total = 0
    i = 1

    while i < n:
        if n % i == 0:
            total = total + i
        i = i + 1

    if total == n:
        print("Perfect number")
    else:
        print("Not a perfect number")
