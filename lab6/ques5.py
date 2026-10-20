n = int(input("Enter number of students: "))

if n < 2 or n > 100:
    print("Invalid number of students")
else:
    winning = 0
    runner_up = 0
    valid = True

    for i in range(n):
        distance = int(input())

        if distance <= 0:
            print("Invalid distance")
            valid = False
            break

        if distance > winning:
            runner_up = winning
            winning = distance
        elif distance < winning and distance > runner_up:
            runner_up = distance

    if valid:
        if runner_up == 0:
            print("At least two different distances are required")
        else:
            print(winning)
            print(runner_up)