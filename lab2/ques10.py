
pounds = float(input("Enter pounds of apples: "))
cash = float(input("Enter cash tendered: "))

cost = pounds * 2.50

if cash >= cost:
    change = cash - cost
    print("Change = $", round(change, 2))
else:
    owed = cost - cash
    print("You owe $", format(owed, ".2f"), "more.")
