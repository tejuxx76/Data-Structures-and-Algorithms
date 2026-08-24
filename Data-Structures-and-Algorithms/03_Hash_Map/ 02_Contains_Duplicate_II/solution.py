def contains_nearby_duplicate(nums, k):

    seen = {}
    for i in range(len(nums)):
        if nums[i] in seen:
            if i - seen[nums[i]] <= k:
                return True
        seen[nums[i]] = i
    return False
# Test
nums = [1, 2, 3, 1]
k = 3
result = contains_nearby_duplicate(nums, k)
if result:
    print("Duplicate found")
else:
    print("No duplicate found")