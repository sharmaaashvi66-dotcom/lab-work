n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid input")
else:
    num = n
    octal = ""

    while num > 0:
        rem = num % 8
        octal = str(rem) + octal
        num = num // 8

    print("Octal equivalent:", octal)

    # Check the answer using the inbuilt oct() function
    if int(octal) == int(oct(n)[2:]):
        print("Both results match")