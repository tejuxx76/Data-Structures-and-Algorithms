s = input("Enter string: ")
k = int(input("Enter k: "))

chars = list(s)

for i in range(0, len(chars), 2 * k):
    left = i
    right = min(i + k - 1, len(chars) - 1)

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
print("Result:", "".join(chars))