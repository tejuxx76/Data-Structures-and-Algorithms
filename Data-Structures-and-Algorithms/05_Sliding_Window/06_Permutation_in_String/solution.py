from collections import Counter

s1 = input("Enter s1: ")
s2 = input("Enter s2: ")

len1, len2 = len(s1), len(s2)

if len1 > len2:
    print("Result: False")
else:
    s1_count = Counter(s1)
    window_count = Counter(s2[:len1])

    if s1_count == window_count:
        print("Result: True")
    else:
        found = False
        for i in range(len1, len2):
            # Add new character entering the window
            window_count[s2[i]] += 1

            # Remove old character leaving the window
            old_char = s2[i - len1]
            if window_count[old_char] == 1:
                del window_count[old_char]
            else:
                window_count[old_char] -= 1

            if s1_count == window_count:
                found = True
                break

        print("Result:", found)