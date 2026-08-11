words = ["flower", "flow", "floght"]
prefix = words[0]

for word in words:
    while not word.startswith(prefix):
        prefix = prefix[:-1]
print("Longest Common Prefix:", prefix)