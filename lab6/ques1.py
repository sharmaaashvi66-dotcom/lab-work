print("          Addition Table")

print("    ", end="")
for i in range(1, 10):
    print(i, end="  ")

print()
print("---------------------------------------")

i = 1
while i <= 9:
    print(i, "|", end="  ")

    j = 1
    while j <= 9:
        print(i + j, end="  ")
        j += 1

    print()
    i += 1