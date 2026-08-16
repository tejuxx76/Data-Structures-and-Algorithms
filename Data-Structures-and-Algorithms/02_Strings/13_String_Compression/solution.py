chars = ["a", "a", "b", "b", "c", "c", "c"]
result = []
i = 0
while i < len(chars):
    char = chars[i]
    count = 0
    while i < len(chars) and chars[i] == char:
        count += 1
        i += 1
    result.append(char)
    if count > 1:
        result.append(str(count))
print("Compressed:", result)