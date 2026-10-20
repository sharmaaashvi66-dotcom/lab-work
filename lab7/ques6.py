s = input("Enter a string: ")
shift = int(input("Enter the shift: "))
result = ""

shift = shift % 26

for ch in s:
    if 'a' <= ch <= 'z':
        new_ch = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        result += new_ch

    elif 'A' <= ch <= 'Z':
        new_ch = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        result += new_ch

print("Encrypted string:", result)