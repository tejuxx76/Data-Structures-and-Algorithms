s = input("Enter first string: ")
t = input("Enter second string: ")

result_s = []
result_t = []
for char in s:
    if char == "#":
        if result_s:
            result_s.pop()
    else:
        result_s.append(char)
for char in t:
    if char == "#":
        if result_t:
            result_t.pop()
    else:
        result_t.append(char)
if result_s == result_t:
    print("Strings are equal")
else:
    print("Strings are not equal")