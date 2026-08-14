s = "egg"
t = "add"

mapping = {}
used = []

isomorphic = True

for i in range(len(s)):

    if s[i] in mapping:
        if mapping[s[i]] != t[i]:
            isomorphic = False
            break

    else:
        if t[i] in used:
            isomorphic = False
            break

        mapping[s[i]] = t[i]
        used.append(t[i])

if isomorphic:
    print("Strings are isomorphic")
else:
    print("Strings are not isomorphic")