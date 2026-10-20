s = input("Enter a sentence: ").lower()
alphabet = "abcdefghijklmnopqrstuvwxyz"
is_pangram = True

for ch in alphabet:
    if ch not in s:
        is_pangram = False
        break

if is_pangram:
    print("The sentence is a pangram")
else:
    print("The sentence is not a pangram")