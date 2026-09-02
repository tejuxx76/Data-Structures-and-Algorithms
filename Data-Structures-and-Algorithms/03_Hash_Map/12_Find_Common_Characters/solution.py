words = input("Enter words separated by space: ").split()

common_counts = {}
for char in words[0]:
    common_counts[char] = common_counts.get(char, 0) + 1

for word in words[1:]:
    current_counts = {}
    for char in word:
        current_counts[char] = current_counts.get(char, 0) + 1

    for char in list(common_counts.keys()):
        if char in current_counts:
            common_counts[char] = min(common_counts[char], current_counts[char])
        else:
            del common_counts[char]
result = []
for char, count in common_counts.items():
    result.extend([char] * count)
print("Common Characters:", result)