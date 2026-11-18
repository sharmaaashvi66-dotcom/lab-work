n = int(input("enter"))
stock = {}
for i in range(n):
    item, qty = input().split()
    stock[item] = int(qty)
q = int(input("enter"))
for i in range(q):
    action, item, qty = input().split()
    qty = int(qty)
    if action == "SELL":
        if stock[item] >= qty:
            stock[item] = stock[item] - qty
        else:
            print("Insufficient stock:", item)

    elif action == "ADD":
        if item in stock:
            stock[item] = stock[item] + qty
        else:
            stock[item] = qty
for item in stock:
    print(item, stock[item])