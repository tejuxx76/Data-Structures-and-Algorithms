s = "tbabtejej"

longest = ""

for i in range(len(s)):

    for j in range(i + 1, len(s) + 1):

        text = s[i:j]

        if text == text[::-1] and len(text) > len(longest):
            longest = text

print("Longest Palindromic Substring:", longest)