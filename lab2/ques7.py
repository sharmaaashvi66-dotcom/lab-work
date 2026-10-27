
color = input("Enter the color (Blue or Red): ").lower()
mode = input("Enter the mode (Steady or Flashing): ").lower()

if color == "blue":
    if mode == "steady":
        print("Clear view")
    else:
        print("Clouds due")
elif color == "red":
    if mode == "steady":
        print("Rain ahead")
    else:
        print("Snow instead")
else:
    print("Invalid input")
