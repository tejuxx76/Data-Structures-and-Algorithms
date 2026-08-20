s = "ADOBECODEBANC"
t = "ABC"
smallest = ""
for i in range(len(s)):
    current = ""
    for j in range(i, len(s)):
        current += s[j]
        possible = True
        for char in t:
            if current.count(char) < t.count(char):
                possible = False
                break

        if possible:
            if smallest == "" or len(current) < len(smallest):
                smallest = current
            break
print("Minimum Window:", smallest)