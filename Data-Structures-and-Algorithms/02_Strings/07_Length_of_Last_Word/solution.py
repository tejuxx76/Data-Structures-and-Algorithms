def length_of_last_word(s):
    words = s.split()
    return len(words[-1])


# Test
s = "Hello World"

result = length_of_last_word(s)

print("Length of last word:", result)