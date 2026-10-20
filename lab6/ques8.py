# Display repeated-number pattern using nested loops

n = int(input("Enter the number of lines: "))

if n <= 0:
    print("Invalid input")
else:
    for i in range(1, n + 1):
        # Print spaces for the triangle shape
        for j in range(n - i):
            print(" ", end="")

        # Print the current number i times
        for j in range(i):
            print(i, end=" ")

        print()