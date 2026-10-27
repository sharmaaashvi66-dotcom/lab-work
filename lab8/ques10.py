s = input("Enter a string: ")

max_count = 1
count = 1
max_char = s[0]

for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        count = count + 1
    else:
        count = 1

    if count > max_count:
        max_count = count
        max_char = s[i]

print(max_char, max_count)