s = input("Enter hyphen-separated words: ")
words = s.split('-')
n = len(words)

for i in range(n):
    for j in range(0, n - i - 1):
        if words[j] > words[j + 1]:
            temp = words[j]
            words[j] = words[j + 1]
            words[j + 1] = temp

result = ""

for i in range(n):
    if i > 0:
        result += "-"
    result += words[i]

print(result)