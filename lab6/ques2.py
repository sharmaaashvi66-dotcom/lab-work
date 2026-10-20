n = int(input("Enter N: "))

if n < 1 or n > 1000:
    print("Invalid input")
else:
    i = 1

    while i <= 1000:
        if i % n != 0:
            i += 1
            continue

        if i % 4 == 0:
            i += 1
            continue

        print(i, end=" ")
        i += 1