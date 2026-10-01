s = input("Enter string: ")

left = 0
right = len(s) - 1

while left < right:

    if s[left] != s[right]:

        first = s[left + 1:right + 1]
        second = s[left:right]

        if first == first[::-1] or second == second[::-1]:
            print("Valid Palindrome")
        else:
            print("Not a Valid Palindrome")

        break

    left += 1
    right -= 1

else:
    print("Valid Palindrome")