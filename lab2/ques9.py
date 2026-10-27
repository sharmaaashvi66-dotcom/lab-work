
n = int(input("Enter the number of widgets: "))

if n < 0:
    print("Invalid input")
elif n >= 100:
    cost = n * 0.20
    print("Total cost = $", round(cost, 2))
else:
    cost = n * 0.25
    print("Total cost = $", round(cost, 2))
