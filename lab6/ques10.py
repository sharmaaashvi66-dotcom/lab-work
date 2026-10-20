# Display a diamond pattern using nested loops

n = int(input("Enter an odd positive integer: "))

if n <= 0 or n % 2 == 0:
    print("Invalid input")
else:
    mid = n // 2

    # Upper half including the middle row
    for i in range(mid + 1):
        for j in range(mid - i):
            print(" ", end="")

        for j in range(2 * i + 1):
            print("*", end="")

        print()

    # Lower half
    for i in range(mid - 1, -1, -1):
        for j in range(mid - i):
            print(" ", end="")

        for j in range(2 * i + 1):
            print("*", end="")

        print()