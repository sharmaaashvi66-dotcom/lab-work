n = int(input("Enter number of students: "))

if n < 2 or n > 100:
    print("Invalid input")
else:
    first = int(input("Enter distance: "))
    second = None

    largest = first
    runner_up = None

    i = 1

    while i < n:
        distance = int(input("Enter distance: "))

        if distance > largest:
            runner_up = largest
            largest = distance

        elif distance < largest:
            if runner_up is None or distance > runner_up:
                runner_up = distance

        i += 1

    if runner_up is None:
        print("No runner-up distance")
    else:
        print(largest)
        print(runner_up)