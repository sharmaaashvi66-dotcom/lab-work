s = input("Enter a string: ")
palindrome = True

for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
        palindrome = False
        break

if palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")