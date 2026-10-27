s = input("Enter a string: ")

vowels = consonants = digits = spaces = others = 0


for ch in s:
    if ch in "aeiou" and "AEIOU":
        vowels = vowels + 1
    elif ch.isalpha():
        consonants = consonants + 1
    elif ch.isdigit():
        digits = digits + 1
    elif ch == " ":
        spaces = spaces + 1
    else:
        others = others + 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Others:", others)