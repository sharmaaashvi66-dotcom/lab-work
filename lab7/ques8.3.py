a = [int(x) for x in input("Enter integers: ").split()]

if len(a) == 0:
    print("List is empty")
else:
    smallest = a[0]

    for i in range(1, len(a)):
        if a[i] < smallest:
            smallest = a[i]

    print("Smallest element:", smallest)