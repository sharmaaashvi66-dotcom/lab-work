n = int(input("Enter an odd positive number: "))

if n <= 0 or n % 2 == 0:
    print("Invalid input")
else:
    i = 1
    mid = n // 2 + 1

    # Upper half of the diamond
    while i <= mid:
        spaces = mid - i
        stars = 2 * i - 1

        j = 1
        while j <= spaces:
            print(" ", end="")
            j += 1

        j = 1
        while j <= stars:
            print("*", end="")
            j += 1

        print()
        i += 1

    # Lower half of the diamond
    i = mid - 1

    while i >= 1:
        spaces = mid - i
        stars = 2 * i - 1

        j = 1
        while j <= spaces:
            print(" ", end="")
            j += 1

        j = 1
        while j <= stars:
            print("*", end="")
            j += 1

        print()
        i -= 1