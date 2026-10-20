s = input("Enter a sentence: ")
result = ""

for ch in s:
    found = False

    for existing in result:
        if ch == existing:
            found = True
            break

    if not found:
        result += ch

print("String after removing duplicates:", result)