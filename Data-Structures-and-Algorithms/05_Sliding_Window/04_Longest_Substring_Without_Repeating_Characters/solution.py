s = input("Enter string: ")

characters = set()
left = 0
maximum = 0

for right in range(len(s)):

    while s[right] in characters:
        characters.remove(s[left])
        left += 1
    characters.add(s[right])
    maximum = max(maximum, right - left + 1)
print("Longest substring length:", maximum)