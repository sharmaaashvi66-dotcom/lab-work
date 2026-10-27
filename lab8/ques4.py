s = input("Enter a string: ")
ch = input("Enter a character: ")

count = 0
positions = ""

for i in range(len(s)):
    if s[i] == ch:
        count = count + 1
        positions = positions + str(i) + " "

print("Count:", count)

if count == 0:
    print("Positions: -1")
else:
    print("Positions:", positions.strip())