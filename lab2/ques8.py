
cost = float(input("Enter the cost: "))
revenue = float(input("Enter the revenue: "))

if cost == revenue:
    print("Break even")
elif revenue > cost:
    print("Profit =", revenue - cost)
else:
    print("Loss =", cost - revenue)
