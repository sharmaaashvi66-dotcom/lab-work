
n = int(input("Enter number of lines: "))

if n <= 0:
    print("Invalid input")
else:
    i = 1

    while i <= n:
        j = 1
        while j <= i:
            print("*", end=" ")
            j = j + 1
        print()
        i = i + 1
