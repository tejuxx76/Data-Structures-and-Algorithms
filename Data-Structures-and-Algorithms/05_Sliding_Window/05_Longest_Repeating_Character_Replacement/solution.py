s = input("Enter string: ")
k = int(input("Enter k: "))

count = {}
left = 0
maximum = 0
most_frequent = 0

for right in range(len(s)):

    count[s[right]] = count.get(s[right], 0) + 1

    most_frequent = max(most_frequent, count[s[right]])

    while (right - left + 1) - most_frequent > k:
        count[s[left]] -= 1
        left += 1

    maximum = max(maximum, right - left + 1)

print("Longest substring length:", maximum)