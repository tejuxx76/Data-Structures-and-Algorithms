s = input("Enter a string: ")
text = ""

for char in s:
    if char.isalnum():
        text += char.lower()

if text == text[::-1]:
    print("It is a palindrome")
else:
    print("It is not a palindrome")