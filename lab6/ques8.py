n = int(input("Enter N: "))

if n <= 0:
    print("Invalid input")
else:
    i = 1

    while i <= n:
        j = 1

        while j <= i:
            print(i, end=" ")
            j += 1

        print()
        i += 1