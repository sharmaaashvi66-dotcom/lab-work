
n = int(input("Enter a positive number: "))
d = int(input("Enter a digit: "))

if n <= 0 or d < 0 or d > 9:
    print("Invalid input")
else:
    count = 0

    while n > 0:
        digit = n % 10

        if digit == d:
            count = count + 1

        n = n // 10

    print("Count =", count)
