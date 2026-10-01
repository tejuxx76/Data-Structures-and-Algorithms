s = input("Enter string: ")
k = int(input("Enter k: "))

vowels = set("aeiou")

current_vowels = sum(1 for i in range(k) if s[i] in vowels)
max_vowels = current_vowels

for i in range(k, len(s)):
    if s[i] in vowels:
        current_vowels += 1
    if s[i - k] in vowels:
        current_vowels -= 1

    max_vowels = max(max_vowels, current_vowels)

print("Result:", max_vowels)