s = input("Enter a sentence: ")
word = input("Enter a word: ")

if word in s:
    print("Word found")
else:
    print("Word not found")

count = s.count(word)
print("Number of occurrences:", count)