pattern = "abba"
s = "dog cat cat dog"

words = s.split()
pattern_to_word = {}
word_to_pattern = {}
if len(pattern) != len(words):
    print("False")
else:
    result = True
    for i in range(len(pattern)):

        p = pattern[i]
        w = words[i]
        if p in pattern_to_word and pattern_to_word[p] != w:
            result = False
            break
        if w in word_to_pattern and word_to_pattern[w] != p:
            result = False
            break
        pattern_to_word[p] = w
        word_to_pattern[w] = p
    print(result)