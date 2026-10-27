num = input("Enter a positive integer: ")

is_palindrome = True
for i in range(len(num)//2):
    if num[i] != num[-(i+1)]:
        is_palindrome = False
        break

if is_palindrome:
    print(num, "is a Palindrome")
else:
    print(num, "is NOT a Palindrome")
