password = input("Enter password: ")

upper = 0
lower = 0
digit = 0
special = 0

for ch in password:
    if ch.isupper():
        upper = 1
    elif ch.islower():
        lower = 1
    elif ch.isdigit():
        digit = 1
    elif ch != " ":
        special = 1

total = upper + lower + digit + special

if len(password) < 8:
    print("WEAK")
elif total == 4:
    print("STRONG")
elif total == 2 or total == 3:
    print("MODERATE")
else:
    print("WEAK")