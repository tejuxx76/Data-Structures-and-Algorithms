s = "aaa"

count = 0

for i in range(len(s)):

    for j in range(i + 1, len(s) + 1):

        text = s[i:j]

        if text == text[::-1]:
            count += 1

print("Number of Palindromic Substrings:", count)