n = int(input("Enter N: "))

if n < 1:
    print("Invalid input")
else:
    num = 1

    while num <= n:
        temp = num
        digits = 0

        # Count the digits
        while temp > 0:
            digits += 1
            temp = temp // 10

        temp = num
        total = 0

        # Calculate the sum of each digit raised to the number of digits
        while temp > 0:
            digit = temp % 10
            total += digit ** digits
            temp = temp // 10

        if total == num:
            print(num, end=" ")

        num += 1