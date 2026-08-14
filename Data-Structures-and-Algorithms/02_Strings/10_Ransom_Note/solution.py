ransomNote = "a"
magazine = "ab"

possible = True

for char in ransomNote:

    if char in magazine:
        magazine = magazine.replace(char, "", 1)

    else:
        possible = False
        break

if possible:
    print("Ransom note can be created")
else:
    print("Ransom note cannot be created")