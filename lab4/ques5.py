# Question 5: Find the cheapest transportation cost

try:
    n = float(input("Enter distance in kilometers: "))
    period = input("Enter period (day/night): ").lower().strip()

    if n <= 0:
        print("Invalid distance")

    elif period not in ["day", "night"]:
        print("Invalid period")

    else:
        # Taxi price
        if period == "day":
            taxi_price = 33.58 + (37.89 * n)
        else:
            taxi_price = 33.58 + (43.17 * n)

        # Initially taxi is always available
        cheapest_price = taxi_price
        transport = "Taxi"

        # Bus is available for distances >= 20 km
        if n >= 20:
            bus_price = 4.32 * n

            if bus_price < cheapest_price:
                cheapest_price = bus_price
                transport = "Bus"

        # Train is available for distances >= 100 km
        if n >= 100:
            train_price = 2.88 * n

            if train_price < cheapest_price:
                cheapest_price = train_price
                transport = "Train"

        print("Cheapest transport:", transport)
        print("Price: {:.2f} INR".format(cheapest_price))

except ValueError:
    print("Invalid input. Please enter a valid number.")