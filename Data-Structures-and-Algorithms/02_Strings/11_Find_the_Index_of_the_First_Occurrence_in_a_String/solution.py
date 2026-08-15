def find_index(haystack, needle):
    return haystack.find(needle)


# Test
haystack = "abdsadbutsad"
needle = "sad"

result = find_index(haystack, needle)

print("Index:", result)