def find_max_length(nums):
    longest = 0

    for i in range(len(nums)):
        zeros = 0
        ones = 0
        for j in range(i, len(nums)):
            if nums[j] == 0:
                zeros += 1
            else:
                ones += 1
            if zeros == ones:
                length = j - i + 1
                if length > longest:
                    longest = length
    return longest
# Test
nums = [0, 1, 0]
print("Longest length:", find_max_length(nums))