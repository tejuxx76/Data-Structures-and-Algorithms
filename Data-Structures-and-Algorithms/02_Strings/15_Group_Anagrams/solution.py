def group_anagrams(words):

    groups = {}

    for word in words:

        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


# Test
words = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = group_anagrams(words)

print("Groups:", result)