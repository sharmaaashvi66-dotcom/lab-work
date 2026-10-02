# Question 7: Determine vacation destination, accommodation and cost

try:
    budget = float(input("Enter your budget in BGN: "))
    season = input("Enter season (summer/winter): ").lower().strip()

    if budget <= 0:
        print("Invalid budget")

    elif season not in ["summer", "winter"]:
        print("Invalid season")

    else:
        # Budget up to 100 BGN
        if budget <= 100:
            destination = "Bulgaria"

            if season == "summer":
                accommodation = "Camp"
                spent = budget * 0.30
            else:
                accommodation = "Hotel"
                spent = budget * 0.70

        # Budget up to 1000 BGN
        elif budget <= 1000:
            destination = "Balkans"

            if season == "summer":
                accommodation = "Camp"
                spent = budget * 0.40
            else:
                accommodation = "Hotel"
                spent = budget * 0.80

        # Budget above 1000 BGN
        else:
            destination = "Europe"
            accommodation = "Hotel"
            spent = budget * 0.90

        print("Somewhere in", destination)
        print(accommodation, "- {:.2f} BGN".format(spent))

except ValueError:
    print("Invalid input. Please enter a valid budget.")