count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
total = 0

while True:
    n = int(input("Enter a number (1-10) or -1 to stop: "))

    if n == -1:
        break

    if n < 1 or n > 10:
        print("Invalid input. Enter a number from 1 to 10.")
        continue

    total += 1

    if n <= 2:
        count1 += 1
    elif n <= 4:
        count2 += 1
    elif n <= 6:
        count3 += 1
    elif n <= 8:
        count4 += 1
    else:
        count5 += 1

if total > 0:
    print("1 - 2:", "# " * count1,
          "%.2f" % (count1 / total * 100), "%")
    print("3 - 4:", "# " * count2,
          "%.2f" % (count2 / total * 100), "%")
    print("5 - 6:", "# " * count3,
          "%.2f" % (count3 / total * 100), "%")
    print("7 - 8:", "# " * count4,
          "%.2f" % (count4 / total * 100), "%")
    print("9 - 10:", "# " * count5,
          "%.2f" % (count5 / total * 100), "%")
else:
    print("No numbers entered.")