# Display the addition table from 1 to 9

print("          Addition Table")
print("   ", end="")

for i in range(1, 10):
    print(i, end="  ")
print()

print("---------------------------------------")

for i in range(1, 10):
    print(i, "|", end=" ")
    for j in range(1, 10):
        print(i + j, end="  ")
    print()