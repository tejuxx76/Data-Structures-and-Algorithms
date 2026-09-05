s = input("Enter string: ")

left = 0
right = len(s) - 1
valid = True

while left < right:

    if s[left] != s[right]:
        left_part = s[left + 1:right + 1]
        right_part = s[left:right]
        if left_part == left_part[::-1] or right_part == right_part[::-1]:
            valid = True
        else:
            valid = False
        break

    left += 1
    right -= 1

if valid:
    print("Valid Palindrome")
else:
    print("Not a Valid Palidrome")