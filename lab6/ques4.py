n = int(input("Enter a positive integer: "))

if n <= 0:
    print("Invalid input")
else:
    num = n
    octal = ""

    while num > 0:
        remainder = num % 8
        octal = str(remainder) + octal
        num = num // 8

    print("Octal equivalent:", octal)

    if octal == str(oct(n))[2:]:
        print("Conversion verified")
    else:
        print("Conversion incorrect")