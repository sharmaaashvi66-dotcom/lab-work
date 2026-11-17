def count_vowels(s):
    count = 0
    for i in s:
        if i.lower() in "aeiou":
            count = count + 1
    return count

s = input()
result = count_vowels(s)
print("Vowels:", result)